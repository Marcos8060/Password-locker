import unittest
from user import User

class TestUser(unittest.TestCase):
    
    # cleanup method after every test case
    def tearDown(self):
        User.contact_list = []

    # method that runs before each test case
    def setUp(self):
        self.new_User = User('marcos','1234567')

    # method to confirm that the object has been instantiated correctly
    def test_init(self):
        self.assertEqual(self.new_User.user_name,'marcos')
        self.assertEqual(self.new_User.password,'1234567')

if __name__ == '__main__':
    unittest.main()