import pdb
from statistics import median_grouped
from models.member import Member
from models.fitness_class import FitnessClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
fitness_class_repository.delete_all()
member_repository.delete_all()

member_repository.save(member)

member_repository.update(member)

member_repository.select(id)

member_repository.select_all()

member_repository.delete(id)

member_repository.classes(member)

fitness_class_repository.save(fitness_class)

fitness_class_repository.update(fitness_class)

fitness_class_repository.select(id)

fitness_class_repository.select_all()

fitness_class_repository.delete(id)

fitness_class_repository.members(fitness_class)

booking_repository.save(booking)

booking_repository.update(booking)

booking_repository.select(id)

booking_repository.select_all()

booking_repository.delete(id)

booking_repository.member(booking)

booking_repository.fitness_class(booking)


pdb.set_trace()