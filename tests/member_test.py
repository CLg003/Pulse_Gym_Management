import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member("Jessica", "Fletcher", "698 Candlewood Lane, Cabot Cove", "jessica.fletcher@email.com")

    def test_member_has_first_name(self):
        self.assertEqual("Sarah", self.member_1.first_name)

    def test_member_has_last_name(self):
        self.assertEqual("Kent", self.member_1.last_name)

    def test_member_has_address(self):
        self.assertEqual("698 Candlewood Lane, Cabot Cove", self.member_1.address)

    def test_member_has_email(self):
        self.assertEqual("sarah.kent@email.com", self.member_1.email)