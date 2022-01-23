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
    
    # method to test saving a user
    def test_save_user(self):
        self.new_User.save_user()
        self.assertEqual(len(User.contact_list),1)

    # method to test deleting a user
    def test_delete_user(self):
        self.new_User.save_user()
        test_user = User('test','1234')
        test_user.save_user()

        self.new_User.delete_user()
        self.assertEqual(len(User.contact_list),1)

if __name__ == '__main__':
    unittest.main()