import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member("Sarah", "Kent", "698 Candlewood Lane, Cabot Cove", "sarah.kent@email.com")

    