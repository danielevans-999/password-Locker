
#!
from passw import User
from passw import Credential
import random


def create_credential(name, password):
    '''
    Function that create  new account and the credentials
    '''
    new_credential = Credential(name, password)
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


def delete_credential(credentials):
    '''
    Function that deletes credentials that are no longer in use
    '''
    return credentials.delete_credential(credentials)


def display_credential():
    '''
    Functiomn that displays all the saved credentials 
    '''
    Credential.display_credentials()

def main():
    
    print('Hello There')
    
    while True:
        print("Use this short codes:cc-Create New User, lgn-To login to your account,ex-to exit")
        short_code = input().lower()
        print('\n')
        
        if short_code == 'cc':
            print("Sign Up")
            my_User_name = input()
            
            print('Your new Password?')
            my_password = input()
            
            print('Confrim your password')
            confirmed_password = input()
            
            # Checking whether the inputted password is the same as the confirmed password
            
            if my_password != confirmed_password:
                print('Oops seem that the password did not match') 
                my_password = input()
                print('Confirm your password')
                confirmed_password = input()
            else:
                print('You have succesfully created a new account')
                print('\n')
                print('Log in to your Account')
                print('Username')
                log_name = input()
                print('password')
                log_password = input()
            
            # checking whether the inpputted details correspond to the sign up details
            
            if log_name != my_User_name or log_password != my_password:
                 print('Wrong username or password')
                 print("Username")
                 log_name = input()
                 print("Your Password")
                 log_password = input()
                 
            else:
                print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                print('\n')
            
                     
                     