from tkinter import Frame,Label,Entry,Button,messagebox,PhotoImage
from BusinessLogicLayer.user_register import Registery
from ComonLayer.Entites.password_entry_show import change_show_mode_to_show,change_show_mode_to_hide


class RegisterFrame(Frame):
    def __init__(self,window,main_view):
        super().__init__(window)

        self.main_view=main_view
        self.add_new_user=Registery()

        self.title_label=Label(self,text='Register Form')
        self.title_label.place(x=50,y=20,anchor='n')

        self.firstname_label=Label(self,text='firstname')
        self.firstname_label.place(x=-150,y=0,anchor='e',relx=0.5,rely=0.25)

        self.firstname_entry=Entry(self)
        self.firstname_entry.place(x=-125,y=0,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        self.lastname_label=Label(self,text='lastname')
        self.lastname_label.place(x=-150,y=50,anchor='e',relx=0.5,rely=0.25)

        self.lastname_entry=Entry(self)
        self.lastname_entry.place(x=-125,y=50,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        self.username_label=Label(self,text='username')
        self.username_label.place(x=-150,y=100,anchor='e',relx=0.5,rely=0.25)

        self.username_entry=Entry(self)
        self.username_entry.place(x=-125,y=100,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        self.password_label1=Label(self,text='password')
        self.password_label1.place(x=-150,y=150,anchor='e',relx=0.5,rely=0.25)

        self.password_entry1=Entry(self,show='*')
        self.password_entry1.place(x=-125,y=150,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        self.password_label2=Label(self,text='confirm password')
        self.password_label2.place(x=-150,y=200,anchor='e',relx=0.5,rely=0.25)

        self.password_entry2=Entry(self,show='*')
        self.password_entry2.place(x=-125,y=200,anchor='w',relx=0.5,rely=0.25,relwidth=0.25)

        # visible=PhotoImage(file='assets/visible.png')
        # self.password_button=Button(self,image=visible,command=lambda:change_show_mode(self.password_button,self.password_entry),width=20,height=20)        
        self.password_button1_show=Button(self,text='O',command=lambda:change_show_mode_to_show(self.password_button1_show,self.password_button1_hide,[-75,150],self.password_entry1),width=2,height=1)
        self.password_button1_show.place(x=-75,y=150,anchor='e',relx=0.75,rely=0.25)
        self.password_button1_hide=Button(self,text='X',command=lambda:change_show_mode_to_hide(self.password_button1_hide,self.password_button1_show,[-75,150],self.password_entry1),width=2,height=1)
        self.password_button1_hide.place_forget()

        self.password_button2_show=Button(self,text='O',command=lambda:change_show_mode_to_show(self.password_button2_show,self.password_button2_hide,[-75,200],self.password_entry2),width=2,height=1)
        self.password_button2_show.place(x=-75,y=200,anchor='e',relx=0.75,rely=0.25)
        self.password_button2_hide=Button(self,text='X',command=lambda:change_show_mode_to_hide(self.password_button2_hide,self.password_button2_show,[-75,200],self.password_entry2),width=2,height=1)
        self.password_button2_hide.place_forget()

        self.register_button=Button(self,text='Register',command=self.registered)
        self.register_button.place(x=-25,y=200,anchor='e',relx=0.8,rely=0.25)

    def registered(self):
        firstname=self.firstname_entry.get()
        lastname=self.lastname_entry.get()
        username=self.username_entry.get()
        password1=self.password_entry1.get()
        password2=self.password_entry2.get()

        register_response=self.add_new_user.add_new_user(firstname,lastname,username,password1,password2)

        if register_response.success:
            self.main_view.switch_frame('Login')
        else:
            messagebox.showerror('Error',register_response.massage)