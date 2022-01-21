class User:
    user_credentials =[]
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password


def save_Credentials(self):
    User.user_credentials.append(self)
