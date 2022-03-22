from flask import Blueprint, render_template, request, redirect

from models.member import Member

import repositories.member_repository as member_repository

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template('members/index.html', members=members, title='Members')

@members_blueprint.route('/members/new', methods=['GET'])
def new_member():
    return render_template('members/new.html', title='New Member')

@members_blueprint.route('/members', methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    email = request.form['email']
    member = Member(first_name, last_name, address, email)
    member_repository.save(member)
    return redirect('/members')

@members_blueprint.route('/members/<id>', methods=['GET'])
def show_member(id):
    member = member_repository.select(id)
    bookings = member_repository.bookings(member)
    return render_template('members/show.html', member=member, bookings=bookings, title='Member Details')

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
    member = Member(first_name, last_name, address, email, id)
    member_repository.update(member)
    return redirect('/members')   

@members_blueprint.route('/members/<id>/delete', methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')

