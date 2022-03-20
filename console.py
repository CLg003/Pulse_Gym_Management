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

# member_1.first_name = "Joey"
# member_repository.update(member_1)

# members = member_repository.select_all()
# for member in members:
#     print(member.__dict__)

# member = member_repository.select(member_2.id)
# print(member.__dict__)

# member_repository.delete(member_1.id)


class_1 = FitnessClass("Yoga", "Mind & Body", "Monday", "19:00")
fitness_class_repository.save(class_1)
class_2 = FitnessClass("Circuits", "Gym", "Tuesday", "07:00")
fitness_class_repository.save(class_2)

# class_1.name = "Body Balance"
# fitness_class_repository.update(class_1)

# fitness_classes = fitness_class_repository.select_all()
# for fitness_class in fitness_classes:
#     print(fitness_class.__dict__)

# fitness_class = fitness_class_repository.select(class_2.id)
# print(fitness_class.__dict__)

# fitness_class_repository.delete(class_2.id)

booking_1 = Booking(member_1, class_1)
booking_repository.save(booking_1)
booking_2 = Booking(member_1, class_2)
booking_repository.save(booking_2)
booking_3 = Booking(member_2, class_2)
booking_repository.save(booking_3)

# booking_1.fitness_class = class_2
# booking_repository.update(booking_1)

# bookings = booking_repository.select_all()
# for booking in bookings:
#     print(booking.__dict__)

# booking = booking_repository.select(booking_1.id)
# print(booking.__dict__)

# booking_repository.delete(booking_1.id)



# STILL TO WRITE:

# fitness_classes = member_repository.fitness_classes(member_1)
# for fitness_class in fitness_classes:
#     print(fitness_class.__dict__)

# members = fitness_class_repository.members(class_1)
# for member in members:
#     print(member.__dict__)

# bookings = member_repository.bookings(member_1)
# for booking in bookings:
#     print(booking.__dict__)

bookings = fitness_class_repository.bookings(class_2)
for booking in bookings:
    print(booking.__dict__)


pdb.set_trace()