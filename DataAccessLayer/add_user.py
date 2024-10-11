import sqlite3
from DataAccessLayer import database_name

class AddUser:
    def add_user(self,firstname,lastname,username,password):
        with sqlite3.connect(database_name) as connection:
            cursor=connection.cursor()
            cursor.execute('''
            INSERT INTO User (
                firstname,
                lastname,
                username,
                password
            )
            VALUES (
                ?,
                ?,
                ?,
                ?);''',(firstname,lastname,username,password))
            connection.commit()
    def get_usernames(self,username):
        with sqlite3.connect(database_name) as connection:
            cursor=connection.cursor()
            cursor.execute('''
            SELECT username
            FROM User
            WHERE username = ?;''',(username,))
        
        usernames=cursor.fetchone()
        return usernames