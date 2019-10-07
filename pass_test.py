
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

        self.new_user = User('daniel', '123')
        self.new_credential = Credential('twiter', '456')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''

        User.user_list = []
        Credential.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is intialized
        '''

        self.assertEqual(self.new_user.user_name, "daniel")
        self.assertEqual(self.new_user.password, "123")
        self.assertEqual(self.new_credential.account_name, "twiter")
        self.assertEqual(self.new_credential.account_password, "456")
        
    def test_save_object(self):
        '''
        test_save_object test case to test if the 
         objects are saved into 
        the user list amd the credential list
        '''    
        
        self.new_user.save_detail()
        self.new_credential.save_credential()
        
        self.assertEqual(len(User.user_list),1)
        self.assertEqual(len(Credential.credentials_list),1)
        


if __name__ == '__main__':
    unittest.main()
