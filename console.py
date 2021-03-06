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
member_6 = Member("Phileas", "Fogg", "7 Savile Row, Burlington Gardens, London", "phileas.fogg@email.com")
member_repository.save(member_6)
member_7 = Member("Mary", "Poppins", "17 Cherry Tree Lane, London", "mary.poppins@email.com")
member_repository.save(member_7)
member_8 = Member("Dudley", "Dursley", "4 Privet Drive, Little Whinging, Surrey", "dudley.dursley@email.com")
member_repository.save(member_8)
member_9 = Member("Harry", "Potter", "4 Privet Drive, Little Whinging, Surrey", "harry.potter@email.com")
member_repository.save(member_9)
member_10 = Member("Eric", "Wimp", "29 Acacia Road", "eric.wimp@email.com")
member_repository.save(member_10)
member_11 = Member("Frasier", "Crane", "Apartment 1901, Elliott Bay Towers, Seattle", "frasier.crane@email.com")
member_repository.save(member_11)
member_12 = Member("John", "Dolittle", "Oxenthorpe Road, Puddleby-on-the-Marsh, Slopshire", "john.dolittle@email.com")
member_repository.save(member_12)
member_13 = Member("Victor", "Meldrew", "19 Riverbank", "holly.golightly@email.com")
member_repository.save(member_13)
member_14 = Member("Clark", "Kent", "344 Clinton St., Apt. 3B, Metropolis", "clark.kent@email.com")
member_repository.save(member_14)
member_15 = Member("Rab", "Nesbit", "32 Restitution Avenue", "holly.golightly@email.com")
member_repository.save(member_15)
member_16 = Member("Tony", "Soprano", "633 Stagtrail Rd. N, Caldwell, New Jersey", "tony.soprano@email.com")
member_repository.save(member_16)
member_17 = Member("Buffy", "Summers", "1630 Revello Drive, Sunnydale", "buffy.summers@email.com")
member_repository.save(member_17)
member_18 = Member("Charles", "Xavier", "1407 Graymalkin Lane, Salem Center, New York", "charles.xavier@email.com")
member_repository.save(member_18)
member_19 = Member("Hyacinth", "Bucket", "117 Blossom Avenue", "hyacinth.bucket@email.com")
member_repository.save(member_19)
member_20 = Member("Fred", "Flinstone", "342 Gravelpit Terrace", "fred.flinstone@email.com")
member_repository.save(member_20)

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

booking_1 = Booking(member_2, class_1)
booking_repository.save(booking_1)
booking_2 = Booking(member_3, class_1)
booking_repository.save(booking_2)
booking_3 = Booking(member_4, class_1)
booking_repository.save(booking_3)
booking_4 = Booking(member_2, class_2)
booking_repository.save(booking_4)
booking_5 = Booking(member_3, class_2)
booking_repository.save(booking_5)
booking_6 = Booking(member_4, class_4)
booking_repository.save(booking_6)
booking_7 = Booking(member_5, class_4)
booking_repository.save(booking_7)
booking_8 = Booking(member_6, class_4)
booking_repository.save(booking_8)
booking_9 = Booking(member_7, class_4)
booking_repository.save(booking_9)
booking_10 = Booking(member_8, class_5)
booking_repository.save(booking_10)
booking_11 = Booking(member_8, class_6)
booking_repository.save(booking_11)
booking_12 = Booking(member_9, class_6)
booking_repository.save(booking_12)
booking_13 = Booking(member_10, class_7)
booking_repository.save(booking_13)
booking_14 = Booking(member_11, class_7)
booking_repository.save(booking_14)
booking_15 = Booking(member_14, class_7)
booking_repository.save(booking_15)
booking_16 = Booking(member_18, class_7)
booking_repository.save(booking_16)
booking_17 = Booking(member_20, class_7)
booking_repository.save(booking_17)
booking_18 = Booking(member_16, class_8)
booking_repository.save(booking_18)
booking_19 = Booking(member_16, class_9)
booking_repository.save(booking_19)
booking_20 = Booking(member_17, class_9)
booking_repository.save(booking_20)
booking_21 = Booking(member_20, class_10)
booking_repository.save(booking_21)
booking_22 = Booking(member_15, class_10)
booking_repository.save(booking_22)
booking_23 = Booking(member_14, class_10)
booking_repository.save(booking_23)
booking_24 = Booking(member_2, class_10)
booking_repository.save(booking_24)
booking_25 = Booking(member_4, class_10)
booking_repository.save(booking_25)
booking_26 = Booking(member_3, class_11)
booking_repository.save(booking_26)
booking_27 = Booking(member_14, class_11)
booking_repository.save(booking_27)
booking_28 = Booking(member_19, class_11)
booking_repository.save(booking_28)
booking_29 = Booking(member_2, class_11)
booking_repository.save(booking_29)
booking_30 = Booking(member_17, class_11)
booking_repository.save(booking_30)
booking_31 = Booking(member_20, class_12)
booking_repository.save(booking_31)
booking_32 = Booking(member_16, class_12)
booking_repository.save(booking_32)
booking_33 = Booking(member_6, class_12)
booking_repository.save(booking_33)
booking_34 = Booking(member_6, class_13)
booking_repository.save(booking_34)
booking_35 = Booking(member_3, class_13)
booking_repository.save(booking_35)
booking_36 = Booking(member_7, class_14)
booking_repository.save(booking_36)
booking_37 = Booking(member_9, class_14)
booking_repository.save(booking_37)
booking_38 = Booking(member_13, class_14)
booking_repository.save(booking_38)
booking_39 = Booking(member_18, class_14)
booking_repository.save(booking_39)
booking_40 = Booking(member_12, class_14)
booking_repository.save(booking_40)



# Calls used for testing repository functions:

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