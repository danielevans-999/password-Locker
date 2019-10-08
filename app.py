
#!
from passw import User
from passw import Credential
import random


def create_user(name, password):
    '''
    Function that create new user
    '''
    new_user = User(name, password)
    return new_user


def save_user(user):
    '''
    Function that save new user
    '''
    user.save_detail()


def user_exist(name):
    '''
    check if user exists
    '''

    return User.user_exists(name)


def create_credential(acc, name, password):
    '''
    Function that create  new account and the credentials
    '''
    new_credential = Credential(acc, name, password)
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
    return Credential.delete_credential(credentials)


def display_credential():
    '''
    Functiomn that displays all the saved credentials 
    '''
    return Credential.display_credentials()


def main():
    while True:
        print("*** PASSWORD LOCKER ***")
        print('_'*30)
        print("Do you have an account with password Locker? yes/no")
        print("use short 'ex' to  log out")
        option = input().lower()
        if option == "yes":

            print('*** Login ***')
            print('Enter username \n')
            nomname = input()
            print('\n')
            print('Enter password')
            nompass = input()
            authentication = user_exist(nomname)

            if authentication == True:
                print(f"Welcome:{nomname} to your Account ")
                print('*'*40)

                print("Select an option either 1,2,3,4 or 5")
                print('\n')

                while True:
                    print('1:Add credential')
                    print('2:View saved credential')
                    print('3:Delete Credentials')
                    print('4:Search Credentials')
                    print('5:Leave')
                    selected = input()

                    if selected == '1':
                        while True:
                            print('Do you want to proceed? y/n')

                            decision = input().lower()
                            if decision == 'y':
                                print("Enter Account name")
                                accname = input()
                                print("Enter username")
                                uname = input()
                                print("Enter a password")
                                print(
                                    "Do you want a computer generated password ? use 'gp' or 'new' to create your own ")
                                word = input().lower()
                                if word == 'gp':
                                    accpass = random.randint(0, 1000)
                                    print(
                                        f"Account:{accname} Username: {uname} Password:{accpass}")
                                    print('\n')
                                elif word == 'new':
                                    print("Create password")
                                    accpass = input()
                                    print(
                                        f"Account:{accname} Password:{accpass}")

                                else:
                                    print("Invalid choice")
                                save_credential(
                                    create_credential(accname, uname, accpass))
                            elif decision == 'n':
                                break
                            else:
                                print(
                                    "Wrong choice use  either y to continue or n to stop")
                    elif selected == '2':
                        while True:
                            print('view your credenttial below')
                            if display_credential():

                                for creds in display_credential():
                                    print(
                                        f"Account Name:{creds.account_name} Username: {creds.username} Password:{creds.account_password}")

                            else:
                                print('\n')
                                print(
                                    "You don't have any saved credential before \n")

                            print("Do you want to go back yes/no")

                            reverse = input().lower()
                            if reverse == 'yes':
                                break
                            elif reverse == 'no':
                                continue
                            else:
                                print("Please input the correct choice")
                                continue
                    elif selected == '3':
                        while True:
                            print("search for account to delete credential")

                            find = input()
                            if existing_credentials(find):
                                accfind = find_credential(find)
                                print(
                                    "Are you sure you want to delete your account yes/no")
                                done = input().lower()
                                if done == 'yes':
                                    delete_credential(accfind)
                                    print("Accont deleted successfully")
                                    break
                                elif done == "no":
                                    continue
                            else:
                                print("Credentialz does not exist")
                                break
                    elif selected == '4':
                        while True:
                            print("Want to proceed y/n")
                            proc = input().lower()
                            if proc == 'y':
                                print(
                                    "Enter the name of the account to view credential")

                                account = input()

                                if existing_credentials(account):
                                    found = find_credential(account)
                                    print(f"ACCOUNT NAME:{found.account_name}")
                                    print(f"PASSWORD {found.account_password}")
                                else:
                                    print("The account does not exist")
                            elif proc == 'n':
                                break
                            else:
                                print("Enter a valid choice")

                    elif selected == '5':
                        print("Are you sure you want to exit this site yes/no")

                        exit == input().lower()

                        if exit == 'yes':
                            print("logged out successfully")
                            break
                        else:
                            if exit == 'no':
                                continue

                    else:
                        print("options not selected")
                        continue

            else:
                print("The user name does not exist")
                print("Create Account ")
                print('*'*40)
                print('Select Username')
                my_username = input()
                print('\n')
                print('Password \n')
                my_password = input()
                save_user(create_user(my_username, my_password))
                print("signed up successfully")

                # continue

        elif option == "no":

            print("Create Account ")
            print('*'*40)
            print('Select Username')
            my_username = input()
            print('\n')
            print('Password \n')
            my_password = input()

            verification = user_exist(my_username)
            if verification == True:
                print("The username already exists")
            else:
                save_user(create_user(my_username, my_password))

            while True:
                print('*** Login ***')
                print('Enter username \n')
                nomname = input()
                print('\n')
                print('Enter password')
                nompass = input()

                if nomname != my_username or nompass != my_password:
                    print("Wrong password or usename")

                    continue
                else:
                    print(f"Welcome:{nomname} to your Account ")
                    print('*'*40)

                    print("Select an option either 1,2,3,4 or 5")
                    print('\n')

                    while True:
                        print('1:Add credential')
                        print('2:View saved credential')
                        print('3:Delete Credentials')
                        print('4:Search Credentials')
                        print('5:Leave')
                        selected = input()

                        if selected == '1':
                            while True:
                                print('Do you want to proceed? y/n')

                                decision = input().lower()
                                if decision == 'y':
                                    print("Enter Account name")
                                    accname = input()
                                    print("Enter user name")
                                    uname = input()
                                    print("Enter a password")
                                    print(
                                        "Do you want a computer generated password ? use 'gp' or 'new' to create your own ")
                                    word = input().lower()
                                    if word == 'gp':
                                        accpass = random.randint(0, 1000)
                                        print(
                                            f"Account:{accname} username:{uname} Password:{accpass}")
                                        print(f"")
                                        print('\n')
                                    elif word == 'new':
                                        print("Create password")
                                        accpass = input()
                                        print(
                                            f"Account:{accname}  username:{uname} Password:{accpass}")

                                    else:
                                        print("Invalid choice")
                                    save_credential(
                                        create_credential(accname, uname, accpass))
                                elif decision == 'n':
                                    break
                                else:
                                    print(
                                        "Wrong choice use  either y to continue or n to stop")
                        elif selected == '2':
                            while True:
                                print('view your credenttial below')
                                if display_credential():

                                    for creds in display_credential():
                                        print(
                                            f"****Account Name:{creds.account_name} username:{creds.username} Password:{creds.account_password}***")
                                        print(
                                            f"")
                                else:
                                    print('\n')
                                    print(
                                        "You don't have any saved credential before \n")

                                print("Do you want to go back yes/no")

                                reverse = input().lower()
                                if reverse == 'yes':
                                    break
                                elif reverse == 'no':
                                    continue
                                else:
                                    print("Please input the correct choice")
                                    continue
                        elif selected == '3':
                            while True:
                                print("search for account to delete credential")

                                find = input()
                                if existing_credentials(find):
                                    accfind = find_credential(find)
                                    print(
                                        "Are you sure you want to delete your account yes/no")
                                    done = input().lower()
                                    if done == 'yes':
                                        delete_credential(accfind)
                                        print("Accont deleted successfully")
                                        break
                                    elif done == "no":
                                        continue
                                else:
                                    print("Credential does not exist")
                                    break
                        elif selected == '4':
                            while True:
                                print("What to proceed y/n")
                                proc = input().lower()
                                if proc == 'y':
                                    print(
                                        "Enter the name of the account to view credential")

                                    account = input()

                                    if existing_credentials(account):
                                        found = find_credential(account)
                                        print(
                                            f"ACCOUNT NAME:{found.account_name} PASSWORD {found.account_password}")

                                    else:
                                        print("The account does not exist")
                                elif proc == 'n':
                                    break
                                else:
                                    print("Enter a valid choice")

                        elif selected == '5':
                            print("Are you sure you want to exit this site yes/no")

                            exit == input().lower()

                            if exit == 'yes':
                                print("logged out successfully")
                                break
                            else:
                                if exit == 'no':
                                    continue

                        else:
                            print("options not selected")
                            continue

        elif option == 'ex':
            print("Thank you ........")
            break
        else:
            print("You entered a wrong option ")


if __name__ == '__main__':
    main()
