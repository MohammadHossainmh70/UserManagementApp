import sqlite3
from DataAccessLayer import database_name
from ComonLayer.Entites.user import User

class UserDataAccess:
    def get_user_with_username_password(self,username,password):
        with sqlite3.connect(database_name) as connection:
            cursor=connection.cursor()
            cursor.execute(f'''
            SELECT id,
                firstname,
                lastname,
                username,
                password
            FROM User 
            WHERE username = ?
            AND   password = ? ;''',(username,password))

            data=cursor.fetchone()

            if data:
                # user=User(data[0],data[1],data[2],None)
                user = User(*data)
                user.password= None
                return user
            # else: 
            #     return None
    def delete_user_account(self,username):
        with sqlite3.connect(database_name) as connection:
            cursor=connection.cursor()
            cursor.execute('''
            DELETE FROM User
            WHERE  username = ?;''',(username,))

            connection.commit()