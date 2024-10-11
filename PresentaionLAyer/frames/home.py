from tkinter import Frame,Label,Button
from BusinessLogicLayer.delete_user import DeleteUser


class HomeFrame(Frame):
    def __init__(self,window,main_view):
        super().__init__(window)

        self.main_view=main_view
        self.delete_user=DeleteUser()
        self.user_data=None

        # self.grid_columnconfigure(0,weight=1)

        self.welcome_label=Label(self)
        self.welcome_label.place(x=50,y=20)

        self.logout_button=Button(self,text='Logout',command=self.logout)
        self.logout_button.place(x=-125,y=0,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        self.delete_button=Button(self,text='Delete',command=self.delete)
        self.delete_button.place(x=-125,y=50,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)
    
    def set_current_user(self,current_user):
        self.welcome_label.config(text=f'Welcome {current_user.get_fullname()}')
        self.user_data=current_user

    def logout(self):
        self.main_view.switch_frame('Login')
    
    def delete(self):
        self.delete_user.delete_user_with_username(self.user_data.username)
        self.main_view.switch_frame('Login')