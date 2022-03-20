from db.run_sql import run_sql

from models.fitness_class import FitnessClass
from models.member import Member
from models.booking import Booking

def save(fitness_class):
    sql = "INSERT INTO fitness_classes (name, category, day, time) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [fitness_class.name, fitness_class.category, fitness_class.day, fitness_class.time]
    results = run_sql(sql, values)
    id = results[0]['id']
    fitness_class.id = id
    return fitness_class

def update(fitness_class):
    sql = "UPDATE fitness_classes SET (name, category, day, time) = (%s, %s, %s, %s) WHERE id = %s"
    values = [fitness_class.name, fitness_class.category, fitness_class.day, fitness_class.time, fitness_class.id]
    run_sql(sql, values)

def select_all():
    fitness_classes = []
    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)
    for row in results:
        fitness_class = FitnessClass(row['name'], row['category'], row['day'], row['time'], row['id'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def select(id):
    sql = "SELECT * FROM fitness_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    fitness_class = FitnessClass(result['name'], result['category'], result['day'], result['time'], result['id'])
    return fitness_class

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def members(fitness_class):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id INNER JOIN fitness_classes ON fitness_classes.id = bookings.fitness_class_id WHERE bookings.fitness_class_id = %s"
    values = [fitness_class.id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['address'], row['email'], row['id'])
        members.append(member)
    return members

