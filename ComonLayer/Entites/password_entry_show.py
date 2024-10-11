# from tkinter import PhotoImage

entry_show_file_place='assets/password_entry_show.txt'

def change_show_mode_to_show(button,new_button,cordinate,entry):
    # visible=PhotoImage(file='assets/visible.png')
    # invisible=PhotoImage(file='assets/invisible.png')

    # button['image']=visible
    entry.config(show='')
    button.place_forget()
    new_button.place(x=cordinate[0],y=cordinate[1],anchor='e',relx=0.75,rely=0.25)
def change_show_mode_to_hide(button,new_button,cordinate,entry):
    entry.config(show='*')
    button.place_forget()
    new_button.place(x=cordinate[0],y=cordinate[1],anchor='e',relx=0.75,rely=0.25)
