#!/user/bin/python3
'''Deines tests for User class
'''
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''TestUser: Tests class for User class
    '''

    def setUp(self):
        '''Sets up variables for subsequent tests
        '''
        self.my_user = User()
        self.my_user.save()

    def test_user_inherits_from_basemodel(self):
        '''Tests that `User` class inherits from BaseModel
        '''
        self.assertIsInstance(self.my_user, BaseModel)

    def test_email_exists(self):
        '''Tests if `User` object has email attribute
        '''
        self.assertTrue(hasattr(User, 'email'))

    def test_password_exists(self):
        '''Tests that `User` object has password attribute
        '''
        self.assertTrue(hasattr(User, 'password'))

    def test_first_name_exists(self):
        '''Tests that `User` object has first_name attribute
        '''
        self.assertTrue(hasattr(User, 'first_name'))

    def test_last_name_exists(self):
        '''Tests that `User` object has last_name attribute
        '''
        self.assertTrue(hasattr(User, 'last_name'))


if __name__ == "__main__":
    unittest.main()
