from flask import Blueprint, render_template, request, redirect

from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository

bookings_blueprint = Blueprint('bookings', __name__)

@bookings_blueprint.route('/bookings', methods=['GET'])
def bookings():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html', bookings=bookings, title='Bookings')

@bookings_blueprint.route('/bookings/new', methods=['GET'])
def new_booking():
    fitness_classes = fitness_class_repository.select_all()
    sorted_classes = sorted(fitness_classes, key=lambda x: x.time)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    members = member_repository.select_all()
    return render_template('bookings/new.html', fitness_classes=sorted_classes, days=days, members=members, title='New Booking')

@bookings_blueprint.route('/bookings/new', methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    fitness_class_id = request.form['fitness_class_id']
    member = member_repository.select(member_id)
    fitness_class = fitness_class_repository.select(fitness_class_id)
    booking = Booking(member, fitness_class)
    booking_repository.save(booking)
    message = "New booking successfully created."
    return render_template('bookings/show.html', booking=booking, message=message, title='New Booking Details')

@bookings_blueprint.route('/bookings/<id>', methods=['GET'])
def show_booking(id):
    booking = booking_repository.select(id)
    return render_template('bookings/show.html', booking=booking, title='View Booking Details')

@bookings_blueprint.route('/bookings/<id>/edit', methods=['GET'])
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    fitness_classes = fitness_class_repository.select_all()
    sorted_classes = sorted(fitness_classes, key=lambda x: x.time)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render_template('bookings/edit.html', booking=booking, members=members, fitness_classes=sorted_classes, days=days, title='Edit Booking')

@bookings_blueprint.route('/bookings/<id>', methods=['POST'])
def update_booking(id):
    member_id = request.form['member_id']
    fitness_class_id = request.form['fitness_class_id']
    member = member_repository.select(member_id)
    fitness_class = fitness_class_repository.select(fitness_class_id)
    booking = Booking(member, fitness_class, id)
    booking_repository.save(booking)
    message = "Booking successfully updated."
    return render_template('bookings/show.html', message=message, booking=booking, title='Updated Booking Details')

@bookings_blueprint.route('/fitness_classes/<id>/arrived', methods=['POST'])
def arrive(id):
    fitness_class = fitness_class_repository.select(id)
    booking_to_check_in = booking_repository.select(id)
    member = member_repository.select(booking_to_check_in.member.id)
    arrived_booking = booking_repository.check_in(booking_to_check_in)
    bookings = fitness_class_repository.bookings(fitness_class)
    return render_template('fitness_classes/show.html', booking=arrived_booking, fitness_class=fitness_class, member=member, bookings=bookings, title='View Booking Details')

@bookings_blueprint.route('/bookings/<id>/delete', methods=['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    bookings = booking_repository.select_all()
    message = "Booking successfully deleted."
    return render_template('bookings/index.html', message=message, bookings=bookings, title='Bookings')

