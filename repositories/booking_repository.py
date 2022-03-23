from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.fitness_class import FitnessClass

import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, fitness_class_id) VALUES (%s, %s) RETURNING *"
    values = [booking.member.id, booking.fitness_class.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    booking.id = id
    return booking

def update(booking):
    sql = "UPDATE bookings SET (member_id, fitness_class_id, arrived) = (%s, %s, %s) WHERE id = %s"
    values = [booking.member.id, booking.fitness_class.id, booking.arrived, booking.id]
    run_sql(sql, values)

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        member = member_repository.select(row['member_id'])
        fitness_class = fitness_class_repository.select(row['fitness_class_id'])
        booking = Booking(member, fitness_class, row['id'])
        bookings.append(booking)
    return bookings

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result['member_id'])
    fitness_class = fitness_class_repository.select(result['fitness_class_id'])
    booking = Booking(member, fitness_class, result['id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def check_in(booking):
    sql = "UPDATE bookings SET arrived = true WHERE id = %s"
    values = [booking.id]
    run_sql(sql, values)
    return booking