import pdb

from models.member import Member
from models.fitness_class import FitnessClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
fitness_class_repository.delete_all()
member_repository.delete_all()

member_1 = Member("Jessica", "Fletcher", "698 Candlewood Lane, Cabot Cove", "jessica.fletcher@email.com")
member_repository.save(member_1)
member_2 = Member("Sherlock", "Holmes", "221b Baker Street, London", "sherlock.holmes@email.com")
member_repository.save(member_2)
member_3 = Member("Bruce", "Wayne", "1007 Mountain Drive, Gotham City", "bruce.wayne@email.com")
member_repository.save(member_3)
member_4 = Member("Jed", "Bartlet", "1600 Pennsylvania Avenue, Washington, D.C.", "jed.bartlet@email.com")
member_repository.save(member_4)
member_5 = Member("Holly", "Golightly", "350 Fifth Avenue, New York City", "holly.golightly@email.com")
member_repository.save(member_5)


class_1 = FitnessClass("Yoga", "Mind & Body", "Monday", "19:00")
fitness_class_repository.save(class_1)
class_2 = FitnessClass("Circuits", "Gym", "Tuesday", "07:00")
fitness_class_repository.save(class_2)
class_3 = FitnessClass("Pilates", "Mind & Body", "Wednesday", "20:00")
fitness_class_repository.save(class_3)
class_4 = FitnessClass("Weightlifting", "Gym", "Monday", "07:00")
fitness_class_repository.save(class_4)
class_5 = FitnessClass("Body Attack", "Cardio", "Monday", "18:00")
fitness_class_repository.save(class_5)
class_6 = FitnessClass("Body Conditioning", "Gym", "Thursday", "19:00")
fitness_class_repository.save(class_6)
class_7 = FitnessClass("Body Attack", "Cardio", "Friday", "18:00")
fitness_class_repository.save(class_7)
class_8 = FitnessClass("Pound", "Cardio", "Friday", "20:00")
fitness_class_repository.save(class_8)
class_9 = FitnessClass("Circuits", "Gym", "Saturday", "07:00")
fitness_class_repository.save(class_9)
class_10 = FitnessClass("Yoga", "Mind & Body", "Saturday", "10:00")
fitness_class_repository.save(class_10)
class_11 = FitnessClass("Pilates", "Mind & Body", "Saturday", "14:00")
fitness_class_repository.save(class_11)
class_12 = FitnessClass("Weightlifting", "Gym", "Wednesday", "07:00")
fitness_class_repository.save(class_12)
class_13 = FitnessClass("Body Attack", "Cardio", "Sunday", "15:00")
fitness_class_repository.save(class_13)
class_14 = FitnessClass("Circuits", "Gym", "Thursday", "07:00")
fitness_class_repository.save(class_14)

booking_1 = Booking(member_1, class_1)
booking_repository.save(booking_1)
booking_2 = Booking(member_2, class_1)
booking_repository.save(booking_2)
booking_3 = Booking(member_3, class_1)
booking_repository.save(booking_3)
booking_4 = Booking(member_2, class_4)
booking_repository.save(booking_4)
booking_5 = Booking(member_1, class_5)
booking_repository.save(booking_5)
booking_6 = Booking(member_4, class_5)
booking_repository.save(booking_6)
booking_7 = Booking(member_4, class_9)
booking_repository.save(booking_7)
booking_8 = Booking(member_5, class_9)
booking_repository.save(booking_8)
booking_9 = Booking(member_3, class_9)
booking_repository.save(booking_9)
booking_10 = Booking(member_5, class_10)
booking_repository.save(booking_10)
booking_11 = Booking(member_4, class_11)
booking_repository.save(booking_11)
booking_12 = Booking(member_1, class_11)
booking_repository.save(booking_12)
booking_13 = Booking(member_2, class_14)
booking_repository.save(booking_13)
booking_14 = Booking(member_5, class_14)
booking_repository.save(booking_14)
booking_15 = Booking(member_3, class_14)
booking_repository.save(booking_15)

# member_1.first_name = "Joey"
# member_repository.update(member_1)

# members = member_repository.select_all()
# for member in members:
#     print(member.__dict__)

# member = member_repository.select(member_2.id)
# print(member.__dict__)

# member_repository.delete(member_1.id)

# class_1.name = "Body Balance"
# fitness_class_repository.update(class_1)

# fitness_classes = fitness_class_repository.select_all()
# for fitness_class in fitness_classes:
#     print(fitness_class.__dict__)

# fitness_class = fitness_class_repository.select(class_2.id)
# print(fitness_class.__dict__)

# fitness_class_repository.delete(class_2.id)

# booking_1.fitness_class = class_2
# booking_repository.update(booking_1)

# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# booking = booking_repository.select(booking_1.id)
# print(booking.__dict__)

# booking_repository.delete(booking_1.id)

# fitness_classes = member_repository.fitness_classes(member_1)
# for fitness_class in fitness_classes:
#     print(fitness_class.__dict__)

# members = fitness_class_repository.members(class_1)
# for member in members:
#     print(member.__dict__)

# bookings = member_repository.bookings(member_1)
# for booking in bookings:
#     print(booking.__dict__)

# bookings = fitness_class_repository.bookings(class_2)
# for booking in bookings:
#     print(booking.__dict__)

pdb.set_trace()