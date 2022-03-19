import pdb
from statistics import median_grouped
from models.member import Member
from models.fitness_class import FitnessClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.booking_repository as booking_repository

# booking_repository.delete_all()
# fitness_class_repository.delete_all()
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

member = member_repository.select(member_2.id)
print(member.__dict__)

# member_repository.delete(id)

# member_repository.classes(member)

# fitness_class_repository.save(fitness_class)

# fitness_class_repository.update(fitness_class)

# fitness_class_repository.select_all()

# fitness_class_repository.select(id)

# fitness_class_repository.delete(id)

# fitness_class_repository.members(fitness_class)

# booking_repository.save(booking)

# booking_repository.update(booking)

# booking_repository.select_all()

# booking_repository.select(id)

# booking_repository.delete(id)

# booking_repository.member(booking)

# booking_repository.fitness_class(booking)


pdb.set_trace()