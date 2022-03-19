import unittest
from models.fitness_class import FitnessClass

class TestFitnessClass(unittest.TestCase):

    def setUp(self):
        self.class_1 = FitnessClass("Yoga", "Mind & Body", "Monday", "13:00")