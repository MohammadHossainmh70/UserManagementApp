from DataAccessLayer.add_user import AddUser
from ComonLayer.ResponsModels.response import Response

class Registery:
    def __init__(self):
        self.add_user=AddUser()
    
    def add_new_user(self,firstname,lastname,username,password1,password2):
        if len(firstname)<3 or len(lastname)<3 or len(username)<3 or len(password1)<3:
            return Response(False,'invalid data',None)
        if password1!=password2:
            return Response(False,'different password',None)
        if not self.add_user.get_usernames(username):
            self.add_user.add_user(firstname,lastname,username,password1)
            return Response(True,'acount made',None)
        
        return Response(False,'used username',None)

