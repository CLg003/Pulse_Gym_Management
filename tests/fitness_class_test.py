import unittest
from models.fitness_class import FitnessClass

class TestFitnessClass(unittest.TestCase):

    def setUp(self):
        self.class_1 = FitnessClass("Yoga", "Mind & Body", "Monday", "19:00")

    def test_class_has_name(self):
        self.assertEqual("Yoga", self.class_1.name)

    def test_class_has_category(self):
        self.assertEqual("Mind & Body", self.class_1.category)

    def test_class_has_day(self):
        self.assertEqual("Monday", self.class_1.day)

    def test_class_has_time(self):
        self.assertEqual("13:00", self.class_1.time)