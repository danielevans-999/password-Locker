
import unittest
from passw import User
from passw import Credential

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the application behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in
        creating test cases

    ''' 
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User('daniel','123')
        self.new_credential = Credential('twiter','456')