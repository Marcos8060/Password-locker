class User:
    contact_list = []
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

        # save user in the contact_list
    def save_user(self):
        User.contact_list.append(self)

    # delete user from the contact_list
    def delete_user(self):
        User.contact_list.remove(self)

    # display users from the contact_list
    @classmethod
    def display_user(cls):
        return cls.contact_list

   
        

