from DataAccessLayer.user_data_access import UserDataAccess
from ComonLayer.ResponsModels.response import Response

class UserBusinessLogic:
    def __init__(self):
        self.user_data_access= UserDataAccess()

    def logic(self,username,password):
        if len(username)<3 or len(password)<3:
            return Response(False,'invalid requset',None)
        
        user=self.user_data_access.get_user_with_username_password(username,password)

        if not user:
            return Response(False,'Invalid username or password',None)
        
        return Response(True,None,user)
        # else:
        #     return Response(True,None,user)