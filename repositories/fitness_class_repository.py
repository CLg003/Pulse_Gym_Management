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

