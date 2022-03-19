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

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)
