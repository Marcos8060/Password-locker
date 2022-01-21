from json.tool import main
from user import User

def main():
    while True:
        print("Welcome to Marcos Password locker!!")
        print("Kindly select a short code to navigate: select 'c' to create a new account, 'l' to login and 'x' to logout from the application")
        short_code = input().lower()
        print('\n')

        if short_code == 'c':
# create username
            print('create a username')
            new_username = input()
# create password
            print('create a password')
            new_password = input()
# confirm password
            print('confirm password')
            confirm_password = input()
# check passwords match
            while new_password != confirm_password:
                print('passwords do not match')


        
