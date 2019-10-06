
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
        
class Credential:
    '''
    class that creates new instances of credentials
    '''
    
    credentials_list = []
    