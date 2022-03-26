from logging.handlers import MemoryHandler
from db.run_sql import run_sql

from models.member import Member
from models.fitness_class import FitnessClass
from models.booking import Booking

import repositories.fitness_class_repository as fitness_class_repository


def save(member):
    sql = "INSERT INTO members (first_name, last_name, address, email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.address, member.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, address, email, premium, active) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.address, member.email, member.premium, member.active, member.id]
    run_sql(sql, values)

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['address'], row['email'], row['premium'], row['active'], row['id'])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result['first_name'], result['last_name'], result['address'], result['email'], result['premium'], result['active'], id)
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values =[id]
    run_sql(sql, values)

def fitness_classes(member):
    fitness_classes = []
    sql = "SELECT fitness_classes.* FROM fitness_classes INNER JOIN bookings ON bookings.fitness_class_id = fitness_classes.id INNER JOIN members ON members.id = bookings.member_id WHERE bookings.member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    for row in results:
        fitness_class = FitnessClass(row['name'], row['category'], row['day'], row['time'], row['id'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def bookings(member):
    bookings = []
    sql = "SELECT bookings.* FROM bookings INNER JOIN members ON bookings.member_id = members.id WHERE bookings.member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    for row in results:
        member = select(row['member_id'])
        fitness_class = fitness_class_repository.select(row['fitness_class_id'])
        booking = Booking(member, fitness_class, row['arrived'], row['id'])
        bookings.append(booking)
    return bookings