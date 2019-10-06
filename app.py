
#!
from passw import User
from passw import Credential
import random

def create_credential(name,password):
    '''
    Function that create  new account and the credentials
    '''
    new_credential = Credential(name,password)
    return new_credential

def save_credential(credentials): 
    '''
    Function to save the new credential details created
    '''
    credentials.save_credential()
    
def find_credential(account_name):
    '''
    Function that finds credentials by account name
    '''    
    
    return Credential.find_by_name(account_name)

def existing_credentials(name):
    '''
    Functiion that checks if an account really exists
    '''
    return Credential.credential_exists(name)