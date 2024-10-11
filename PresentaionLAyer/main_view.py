from PresentaionLAyer.window import Window
from PresentaionLAyer.frames.login import LoginFrame
from PresentaionLAyer.frames.home import HomeFrame
from PresentaionLAyer.frames.register import RegisterFrame

class MainView:
    def __init__(self):
        self.frames={}
        self.window=Window()

        self.add_frame('Register',RegisterFrame(self.window,self))
        self.add_frame('Home',HomeFrame(self.window,self,))
        self.add_frame('Login',LoginFrame(self.window,self))

        self.window.show()
    def add_frame(self,name,frame):
        self.frames[name]=frame
        frame.place(x=0,y=0,relwidth=1,relheight=1)

    def switch_frame(self,name):
        frame=self.frames[name]
        frame.tkraise()
        return frame