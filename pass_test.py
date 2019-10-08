
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
        self.new_credential = Credential('twiter', 'daniel','456')

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
     
    def test_find_user_by_name(self):
        '''
        test to check if we can find a user or credential by account name and display information
        '''
        
        
        self.new_credential.save_credential()
        found_credential = Credential.find_by_name('twiter')
        self.assertEqual(found_credential.account_password,'456')
        
    def test_credential_exists(self):
        '''test to check if we can return a boolean if we cannot  find the cridential
        test to check if we can return a boolean if we cannot  find the cridential
        '''     
        
        self.new_credential.save_credential()
        credential_exist = Credential.credential_exists("twiter")
        self.assertTrue(credential_exist)
        
    def test_delete_credential(self):
        '''
        Test case to check if the user can delete their credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credential("instagram",'daniel',"789") 
        test_credential.save_credential()
        
        Credential.credentials_list.remove(test_credential)   
        
        self.assertEqual(len(Credential.credentials_list),1)
        
    def test_display_all_credential(self):
        '''
        method that return all the credential saved
        '''    
        
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)
              
        


if __name__ == '__main__':
    unittest.main()
