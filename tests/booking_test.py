import unittest
from models.booking import Booking
from models.member import Member
from models.fitness_class import FitnessClass

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.booking_1 = Booking(self.member_1, self.class_1)

        self.member_1 = Member("Sarah", "Kent", "698 Candlewood Lane, Cabot Cove", "sarah.kent@email.com")

        self.class_1 = FitnessClass("Yoga", "Mind & Body", "Monday", "13:00")