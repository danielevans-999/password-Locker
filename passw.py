
class User:
    '''
    Class that generates new instances of users.
    '''
    
    user_list = []
    
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        
    def save_detail(self):
        '''
        class method that saves the user object into the user_list
        '''    
        
        self.user_list.append(self)
    @classmethod
    def user_exists(cls,name):
        for user in cls.user_list:
            if user.user_name == name:
                return True
        return False
        
class Credential:
    '''
    class that creates new instances of credentials
    '''
    
    credentials_list = []
    
    
    def __init__(self,account_name,username,acount_password):
        self.account_name = account_name
        self.account_password = acount_password
        self. username = username
    
    def save_credential(self):
        '''
        method that saves the the created credential objects to the credential list
        '''
        
        self.credentials_list.append(self)
     
    def delete_credential(self):
        '''
        Method that deletes the crredential that are no longer used from the credential list
        '''    
        
        self.credentials_list.remove(self)
        
    @classmethod
    def find_by_name(cls,account_name):
        '''
        Method that takes in account name and return credential object that matches that account name
         
         Args:
              account name:accountname to search for
        return:
               credential of user that matches the account name      
        '''    
        
        for cred in cls.credentials_list:
            if cred.account_name == account_name:
                return cred
    
    @classmethod    
    def credential_exists(cls,acc_name):
        '''
        Method that checks if a credential object exists from the credential  list.
        Args:
            acc_name: Account  to search if it exists
        Returns :
            Boolean: True or false depending if the object exists
        '''
        
        for creds in cls.credentials_list:
            if creds.account_name == acc_name:
                return True
        return False    
               
    @classmethod
    def display_credentials(cls):
        '''
        Method which will display the credential list
        '''
        return cls.credentials_list           