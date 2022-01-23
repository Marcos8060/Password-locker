import unittest
from user import User

class TestUser(unittest.TestCase):
    
    # cleanup method after every test case
    def tearDown(self):
        User.contact_list = []
