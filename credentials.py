class Credentials:
    # declaring an empty user accounts list
    user_accounts = []
    def __init__(self,user_name,user_password):
        self.user_name = user_name
        self.user_password = user_password

    # method to save a user account
    def save_account(self):
    
        Credentials.user_accounts.append(self)

    # method to delete a user account
    def delete_account(self):

        Credentials.user_accounts.remove(self)

    # method to display accounts
    @classmethod
    def display_accounts(cls):
        for account in cls.user_accounts:
            return cls.user_accounts


   
