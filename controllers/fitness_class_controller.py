from flask import Blueprint, render_template, request, redirect

from models.fitness_class import FitnessClass

import repositories.fitness_class_repository as fitness_class_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

@fitness_classes_blueprint.route("/fitness_classes", methods=['GET'])
def fitness_classes():
    fitness_classes = fitness_class_repository.select_all()
    return render_template("fitness_classes/index.html", fitness_classes=fitness_classes)

@fitness_classes_blueprint.route("/fitness_classes/new", methods=['GET'])
def new_class():
    return render_template("fitness_classes/new.html")