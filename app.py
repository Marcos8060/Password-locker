from asyncio import unix_events
from user import User
from credentials import Credentials
import string
import random

def create_user(user_name,password):
    new_user = User(user_name,password)
    return new_user
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def display_users():
    return User.display_user()

# create account instances
def create_account(user_name,user_password):
    new_account = Credentials(user_name,user_password)
    return new_account
def save_account(user):
    user.save_account()
def delete_account(user):
    user.delete_account()
def display_accounts():
    return Credentials.display_accounts()

# main function for the programme
def main():
    while True:
        print("Thank you for visiting password locker 😊")
        print('To proceed enter a short code "su" to sign up and create an account or "x" to exit')
        short_code = input().lower()
        if short_code == 'su':
            print('Create your account')
            print('Enter your username')
            first_username = input()
            print('Enter password')
            first_password = input()
            print('Confirm password')
            confirm_password = input()

            # check if passwords match
            while first_password != confirm_password:
                print('Passwords do not match 😞')
                print('Enter password')
                first_password = input()
                print('Confirm password')
                confirm_password = input()
            else:
                print(f'Congratulations {first_username} Your account was created successfully. The following are your account details:')
                print(f'Username: {first_username} \nPassword: {first_password}')
                save_user(create_user(first_username,first_password))
                print('\n')
                print('Proceed to login')
                print('Enter username')
                login_username = input()
                print('Enter password')
                login_password = input()

                while login_username != first_username or login_password != first_password:
                   print("Sorry Invalid credentials!!")
                   print('Enter your username')
                   login_username = input()
                   print('Enter password')
                   login_password = input()
                else:
                   print(f'Congratulations {login_username}, welcome to your password locker account \n')
                   print('Did you know you can create multiple accounts with us?, select "ca" to create one.')
                select = input().lower()
                if select == 'ca':
                    print('Enter account username')
                    account_username = input()
                    print('Print "g" to generate a random password or "c" to create your own password')
                    choice = input().lower()
                    if choice == 'g':
                            pass1 = string.ascii_uppercase
                            pass2 = string.ascii_lowercase
                            pass3 = string.digits
                            pass4 = string.punctuation
                            passlength = int(input("Enter your password length\n"))
                            s = []
                            s.extend(list(pass1))
                            s.extend(list(pass2))
                            s.extend(list(pass3))
                            s.extend(list(pass4))
                            random.shuffle(s)
                            account_password = ("".join(s[0:passlength]))
                            print(f'Password: {account_password}')
                            print('Congratulations, your first account was created successfully.')
                            save_account(create_account(account_username,account_password))
                            print('To view your saved accounts, enter "ok": ')
                            selected = input().lower()
                            if selected == 'ok':
                                print('\n')
                                for user in display_accounts():
                                 print(f'Account username: {user.user_name} \nPassword: {user.user_password}')
                                 print('\n')
                    elif choice == 'c':
                        print('Enter your password')
                        account_password = input()
                        print(f'Password: {account_password}')
                        print('Congratulations, your first account was created successfully!!')
                        save_account(create_account(account_username,account_password))
                        print('To view your saved accounts, enter "ok": ')
                        selected = input().lower()
                        print('\n')
                        if selected == 'ok':
                            for user in display_accounts():
                                print(f'Account username: {user.user_name} \nPassword: {user.user_password}')
                                print('\n')
                    else:
                        print('Please enter a valid choice!!')
                        save_account(create_account(account_username,account_password))
                        print('\n')
                else:
                    print('Please try again')
        elif short_code == 'x':
            print('Thank you for visiting password locker')
            break

if __name__ == '__main__':
    main()



# from json.tool import main
# from user import User

# def main():
#     while True:
#         print("Welcome to Password locker!!")
#         print("Kindly select a short code to navigate: select 'c' to create a new account, 'l' to login and 'x' to logout from the application")
#         short_code = input().lower()
#         print('\n')

#         if short_code == 'c':

#             print('create a username')
#             new_username = input()

#             print('create a password')
#             new_password = input()

#             print('confirm password')
#             confirm_password = input()

#             while new_password != confirm_password:

#                 print('passwords do not match!!')
#                 print('create new password')
#                 new_password = input()
#                 print('confirm password')
#                 confirm_password = input()
#             else:

#                 print(f'Congratulations {new_username} your account is created successfully')
#                 print('\n')

#                 print('proceed to login')
#                 print('Enter username')
#                 login_username = input()
#                 print('Enter password')
#                 login_password = input()

#                 while login_username != new_username or login_password != new_password:
#                     print('Sorry you entered wrong cedentials')
#                     print('Try loging in again')
#                     login_username = input()
#                     print('Enter password')
#                     login_password = input()

#                 else:
#                     print(f'congaratulations {login_username}, your login is successful')
#         elif short_code == 'l':
#             print('Enter username')
#             default_username = input()
#             print('Enter password')
#             default_password = input()

#             while default_username != 'hello world' or default_password != '12345':
#                 print('Invalid credentials, you username is "hello world" and password is "12345"')
#                 print("Enter username")
#                 default_username = input()
#                 print('Enter password')
#                 default_password = input()
#             else:
#                 print(f'Congratulations {default_username}, welcome to password locker')
#                 print('/n')
        
#         elif short_code == 'x':
#             break
#         else:
#             print('Enter a valid code to continue')

# if __name__ == '__main__':
#     main()

                




        
