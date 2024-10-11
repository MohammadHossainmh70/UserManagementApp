from tkinter import Frame,Label,Entry,Button,messagebox,PhotoImage
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from ComonLayer.Entites.password_entry_show import change_show_mode_to_show,change_show_mode_to_hide


class LoginFrame(Frame):
    def __init__(self,window,main_view):
        super().__init__(window)

        self.main_view=main_view
        self.user_business_logic=UserBusinessLogic()

        self.title_label=Label(self,text='Login Form')
        self.title_label.place(x=50,y=20,anchor='n')

        self.username_label=Label(self,text='username')
        self.username_label.place(x=-150,y=0,anchor='e',relx=0.5,rely=0.25)

        self.username_entry=Entry(self)
        self.username_entry.place(x=-125,y=0,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        self.password_label=Label(self,text='password')
        self.password_label.place(x=-150,y=50,anchor='e',relx=0.5,rely=0.25)

        self.password_entry=Entry(self,show='*')
        self.password_entry.place(x=-125,y=50,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        # visible=PhotoImage(file='assets/visible.png')
        # self.password_button=Button(self,image=visible,command=lambda:change_show_mode(self.password_button,self.password_entry),width=20,height=20)        
        self.password_button_show=Button(self,text='O',command=lambda:change_show_mode_to_show(self.password_button_show,self.password_button_hide,[-75,50],self.password_entry),width=2,height=1)
        self.password_button_hide=Button(self,text='X',command=lambda:change_show_mode_to_hide(self.password_button_hide,self.password_button_show,[-75,50],self.password_entry),width=2,height=1)
        self.password_button_show.place(x=-75,y=50,anchor='e',relx=0.75,rely=0.25)
        self.password_button_hide.place_forget()

        self.login_button=Button(self,text='Login',command=self.Login)
        self.login_button.place(x=-125,y=100,anchor='w',relx=0.5,rely=0.25)

        self.register_button=Button(self,text='Register',command=self.go_to_register_fram)
        self.register_button.place(x=-125,y=150,anchor='w',relx=0.5,rely=0.25)

    def Login(self):
        username=self.username_entry.get()
        password=self.password_entry.get()

        result=self.user_business_logic.logic(username,password)

        if result.success:
            # messagebox.showinfo('Information',f'Wellcome {result.data.get_fullname()}')
            home_frame=self.main_view.switch_frame('Home')
            home_frame.set_current_user(result.data)

            self.username_entry.delete(0,'end')
            self.password_entry.delete(0,'end')
        else:
            messagebox.showerror('Error',result.massage)
    def go_to_register_fram(self):
        self.main_view.switch_frame('Register')

        self.username_entry.delete(0,'end')
        self.password_entry.delete(0,'end')