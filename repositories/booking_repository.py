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
    sql = "UPDATE bookings SET (member_id, fitness_class_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.fitness_class.id, booking.id]
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
