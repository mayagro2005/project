import threading
import tkinter
from tkinter import *
from add_teachers_or_students import Register
# from login import Login
from tkinter import ttk, messagebox
import socket
import hashlib
from login1 import Login
from PIL import ImageTk, Image


from dbteachers import *
from dbstudents import *
from tkinter import ttk
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('900x800')
        self.title('Main Window')
        # self.configure(bg='pink')
        self.img = Image.open('fitness.png')
        self.resized = self.img.resize((900,800), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.label_image = Label(self,image=self.image)
        self.label_image.place(x=0,y=0)

        # image = Image.open("fitness.png")
        # image = image.resize((800, 800), Image.LANCZOS)
        # pic = ImageTk.PhotoImage(image)
        # # img = Image.open("/Users/mayagrossman/Documents/dog.png")
        # # bg = ImageTk.PhotoImage(img)
        #
        # canvas = Canvas(width=800, height=800)
        # canvas.pack(expand=YES, fill=BOTH)
        #
        # canvas.create_image(0, 0, image=pic, anchor=NW)
        # place a button on the root window

        self.welcome = Label(self, text="Welcome!", background="red",foreground="black", font=("Calibri",25))
        self.welcome.place(x=350, y=50,width=200,height=70)
        self.btn_signup = Button(self, text='SIGN UP', background="white", foreground="black", font=("Calibri",15),command=self.open_register)
        self.btn_signup.place(x=380, y=400, width=140,height=50)

        self.btn_signin = Button(self, text='SIGN IN',background="white", foreground="black", font=("Calibri",15), command=self.open_login)
        self.btn_signin.place(x=380, y=470,width=140,height=50)

        self.handle_thread_socket()

        # self.femail = Label(self, text="Email:", background="light blue")
        # self.femail.place(x=50, y=100)
        # self.etemail = Entry(self)
        # self.etemail.place(x=150, y=100)
        #
        # self.fpassword = Label(self, text="password:", background="light blue")
        # self.fpassword.place(x=50, y=150)
        # self.etpassword = Entry(self)
        # self.etpassword.place(x=150, y=150)

    #     self.btn_login = Button(self, text='login', command=self.login_user)
    #     self.btn_login.place(x=50,y=300)
    #     self.str = StringVar()
    #     self.str.set("")
    #     self.labellogin = Label(self, textvariable=self.str, background="light blue")
    #     self.labellogin.place(x=50, y=200)
    #     self.userdb = User()
    #     self.handle_thread_socket()
    #
    # def login_user(self):
    #     if len(self.etemail.get()) == 0 and len(self.etpassword.get()) == 0:
    #         messagebox.showerror("please write details", "Error")
    #         return
    #     print("login")
    #     if self.userdb.is_exist(self.etemail.get(), self.etpassword.get()) == False:
    #         message = "please register"
    #         self.str.set(message)
    #         print(self.str.get())
    #     else:
    #         message2 = "welcome, you are loged"
    #         self.str.set(message2)
    #         print(self.str.get())





        # arr = ["register", self.email.get(), self.password.get(), self.firstname.get()]
        # str_insert = ",".join(arr)
        # print(str_insert)
        # self.parent.client_socket.send(str_insert.encode())
        # data = self.parent.client_socket.recv(1024).decode()
        # print(data)

    def open_register(self):
        window = Register(self)
        window.grab_set()
        self.withdraw()

    def open_login(self):
        window = Login(self)
        window.grab_set()
        self.withdraw()
    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1803))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)

if __name__ == "__main__":
    app = App()
    app.mainloop()
