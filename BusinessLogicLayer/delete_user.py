from DataAccessLayer.user_data_access import UserDataAccess

class DeleteUser:
    def __init__(self):
        self.user_data_access= UserDataAccess()
    
    def delete_user_with_username(self,username):
        self.user_data_access.delete_user_account(username)