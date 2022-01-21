from json.tool import main
from user import User

def main():
    while True:
        print("Welcome to Password locker!!")
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
# throw error on passwords mismatch
                print('passwords do not match!!')
                print('create new password')
                new_password = input()
                print('confirm password')
                confirm_password = input()
            else:
# send a success message
                print(f'Congratulations {new_username} your account is created successfully')
                print('\n')
# authenticating the user
                print('proceed to login')
                print('Enter username')
                login_username = input()
                print('Enter password')
                login_password = input()

# checking login credentials
                while login_username != new_username or login_password != new_password:
                    print('Sorry you entered wrong cedentials')
                    print('Try loging in again')
                    login_username = input()
                    print('Enter password')
                    login_password = input()

# check if credentials are right upon login
                else:
                    print(f'congaratulations {login_username}, your login is successful')
# first time login 
        elif short_code == 'l':
            print('Enter username')
            default_username = input()
            print('Enter password')
            default_password = input()

            while default_username != 'hello world' or default_password != '12345':
                print('Invalid credentials, you username is "hello world" and password is "12345"')
                print("Enter username")
                default_username = input()
                print('Enter password')
                default_password = input()
            # check if default login credentials are right
            else:
                print(f'Congratulations {default_username}, welcome to password locker')
                print('/n')
        
        # check logout functionality
        elif short_code == 'x':
            break
        else:
            print('Enter a valid code to continue')

if __name__ == '__main__':
    main()

                




        
