from tkinter import Tk

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('User Management Application')
        self.geometry('500x300')

    def show(self):
        self.mainloop()