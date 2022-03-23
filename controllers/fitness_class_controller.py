from flask import Blueprint, render_template, request, redirect

from models.fitness_class import FitnessClass

import repositories.fitness_class_repository as fitness_class_repository

fitness_classes_blueprint = Blueprint('fitness_classes', __name__)

@fitness_classes_blueprint.route('/fitness_classes', methods=['GET'])
def fitness_classes():
    fitness_classes = fitness_class_repository.select_all()
    sorted_classes = sorted(fitness_classes, key=lambda x: x.time)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render_template('fitness_classes/index.html', fitness_classes=sorted_classes, days=days, title='Fitness Classes')

@fitness_classes_blueprint.route('/fitness_classes/new', methods=['GET'])
def new_class():
    return render_template('fitness_classes/new.html', title='New Fitness Class')

@fitness_classes_blueprint.route('/fitness_classes/new', methods=['POST'])
def create_fitness_class():
    name = request.form['name']
    category = request.form['category']
    day = request.form['day']
    time = request.form['time']
    fitness_class = FitnessClass(name, category, day, time)
    fitness_class_repository.save(fitness_class)
    message = "New class successfully created."
    return render_template('fitness_classes/show.html', fitness_class=fitness_class, message=message, title='New Fitness Class Details')

@fitness_classes_blueprint.route('/fitness_classes/<id>', methods=['GET'])
def show_fitness_class(id):
    fitness_class = fitness_class_repository.select(id)
    members = fitness_class_repository.members(fitness_class)
    return render_template('fitness_classes/show.html', fitness_class=fitness_class, members=members, title='Fitness Class Details')

@fitness_classes_blueprint.route('/fitness_classes/<id>/edit', methods=['GET'])
def edit_fitness_class(id):
    fitness_class = fitness_class_repository.select(id)
    fitness_class_categories = fitness_class_repository.select_all_categories()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render_template('fitness_classes/edit.html', fitness_class=fitness_class, fitness_class_categories=fitness_class_categories, days=days, title='Edit Fitness Class')

@fitness_classes_blueprint.route('/fitness_classes/<id>', methods=['POST'])
def update_fitness_class(id):
    name = request.form['name']
    category = request.form['category']
    day = request.form['day']
    time = request.form['time']
    class_status = request.form['fitness-class-status']
    if class_status == "inactive":
        active = False
    else:
        active = True
    fitness_class = FitnessClass(name, category, day, time, active, id)
    fitness_class_repository.update(fitness_class)
    members = fitness_class_repository.members(fitness_class)
    message = "Class successfully updated."
    return render_template('fitness_classes/show.html', message=message, fitness_class=fitness_class, members=members, title='Updated Fitness Class Details')

@fitness_classes_blueprint.route('/fitness_classes/<id>/delete', methods=['POST'])
def delete_fitness_class(id):
    fitness_class_repository.delete(id)
    fitness_classes = fitness_class_repository.select_all()
    sorted_classes = sorted(fitness_classes, key=lambda x: x.time)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    message = "Class successfully deleted."
    return render_template('fitness_classes/index.html', message=message, fitness_classes=sorted_classes, days=days, title='Fitness Classes')