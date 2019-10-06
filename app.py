
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