import unittest
from models.booking import Booking
from models.member import Member
from models.fitness_class import FitnessClass

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member("Jessica", "Fletcher", "698 Candlewood Lane, Cabot Cove", "jessica.fletcher@email.com")
        self.class_1 = FitnessClass("Yoga", "Mind & Body", "Monday", "19:00")
        self.booking_1 = Booking(self.member_1, self.class_1)
        
    
    def test_booking_has_member(self):
        self.assertEqual("Sarah", self.booking_1.member.first_name)

    def test_booking_has_class(self):
        self.assertEqual("Yoga", self.booking_1.fitness_class.name)