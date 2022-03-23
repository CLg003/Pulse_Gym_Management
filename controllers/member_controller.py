from flask import Blueprint, render_template, request, redirect

from models.member import Member

import repositories.member_repository as member_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    sorted_members = sorted(members, key=lambda x: x.id)
    return render_template('members/index.html', members=sorted_members, title='Members')

@members_blueprint.route('/members/new', methods=['GET'])
def new_member():
    return render_template('members/new.html', title='New Member')

@members_blueprint.route('/members/new', methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    email = request.form['email']
    member = Member(first_name, last_name, address, email)
    member_repository.save(member)
    message = "New member successfully created."
    return render_template('members/show.html', member=member, message=message, title='New Member Details')

@members_blueprint.route('/members/<id>', methods=['GET'])
def show_member(id):
    member = member_repository.select(id)
    bookings = member_repository.bookings(member)
    return render_template('members/show.html', member=member, bookings=bookings, title='View Member Details')

@members_blueprint.route('/members/<id>/edit', methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member, title='Edit Member')

@members_blueprint.route('/members/<id>', methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    email = request.form['email']
    membership_level = request.form['membership-level']
    if membership_level == "premium":
        premium = True
    else:
        premium = False
    membership_status = request.form['membership-status']
    if membership_status == "inactive":
        active = False
    else:
        active = True
    member = Member(first_name, last_name, address, email, premium, active, id)
    member_repository.update(member)
    message = "Member details successfully updated."
    return render_template('members/show.html', message=message, member=member, title='Updated Member Details')   

@members_blueprint.route('/members/<id>/delete', methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    members = member_repository.select_all()
    sorted_members = sorted(members, key=lambda x: x.id)
    message = "Member successfully deleted."
    return render_template('members/index.html', message=message, members=sorted_members, title='Members')

