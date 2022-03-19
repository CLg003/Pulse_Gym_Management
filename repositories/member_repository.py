from logging.handlers import MemoryHandler
from db.run_sql import run_sql

from models.member import Member
from models.fitness_class import FitnessClass
from models.booking import Booking


def save(member):
    sql = "INSERT INTO members (first_name, last_name, address, email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.address, member.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, address, email) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.address, member.email, member.id]
    run_sql(sql, values)

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['address'], row['email'], row['id'])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result['first_name'], result['last_name'], result['address'], result['email'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values =[id]
    run_sql(sql, values)