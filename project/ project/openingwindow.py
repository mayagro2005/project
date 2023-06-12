import struct
import threading
import tkinter
from tkinter import *
from add_teachers_or_students import Register
# from login import Login
from tkinter import ttk, messagebox, font
import socket
import hashlib
from login1 import Login
from PIL import ImageTk, Image
from tkmacosx import Button
from cryptography.hazmat.primitives import serialization

SIZE = 12
from dbteachers import *
from dbstudents import *
from tkinter import ttk

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1100x680')
        self.title('OPENING WINDOW')
        # self.configure(bg='#F3CCFF')
        self.format = 'utf-8'
        self.img = Image.open('istock.png')
        self.resized = self.img.resize((1100,680), Image.LANCZOS)
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

        # self.welcome = Label(self, text="Welcome", background="white",foreground="black", font=("Calibri",25))
        # self.welcome.place(x=350, y=50,width=200,height=70)
        # # self.btn_signup = Button(self, text='SIGN UP', background="white", foreground="black", font=("Calibri",15),command=self.open_register)
        # self.btn_signup= Button(self, text='SIGN UP', activeforeground='#EE3B3B', overrelief='flat', relief='flat', borderwidth=2,
        #             highlightthickness=1, font=font.Font(family='SignPainter', size=30, weight='bold', slant='roman'),
        #             focuscolor='#556B2F', highlightbackground='#CD5555', foreground='#1F1F1F', background='#7A7A7A',
        #             overbackground='#000000', overforeground='#00C78C', activebackground=('#BA55D3', '#D4D4D4'),
        #             borderless=1,command=self.open_register)
        # self.btn_signup.place(x=380, y=400, width=140,height=50)
        #
        # # self.btn_signin = Button(self, text='SIGN IN',background="white", foreground="black", font=("Calibri",15), command=self.open_login)
        # self.btn_signin = Button(self, text='SIGN IN', activeforeground='#EE3B3B', overrelief='flat', relief='flat',
        #                          borderwidth=2,
        #                          highlightthickness=1,
        #                          font=font.Font(family='SignPainter', size=30, weight='bold', slant='roman'),
        #                          focuscolor='#556B2F', highlightbackground='#CD5555', foreground='#1F1F1F',
        #                          background='#7A7A7A',
        #                          overbackground='#000000', overforeground='#00C78C',
        #                          activebackground=('#BA55D3', '#D4D4D4'),
        #                          borderless=1, command=self.open_login)
        # self.btn_signin.place(x=380, y=470,width=140,height=50)
        self.welcome = Label(self, text="Welcome", background="white", foreground="black", font=("Calibri", 40, "bold"))
        self.welcome.config(bd=5, relief="groove")
        self.welcome.config(highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.welcome.place(x=400, y=20, width=300, height=100)

        self.btn_signup = Button(self, text='SIGN UP', activeforeground='#EE3B3B', font=("Calibri", 25, "bold"),
                                 command=self.open_register)
        self.btn_signup.config(bg='#7A7A7A', fg='white', bd=5, relief="raised", highlightbackground="black",
                               highlightcolor="black", highlightthickness=2)
        self.btn_signup.place(x=330, y=570, width=200, height=70)

        self.btn_signin = Button(self, text='SIGN IN', activeforeground='#EE3B3B', font=("Calibri", 25, "bold"),
                                 command=self.open_login)
        self.btn_signin.config(bg='#7A7A7A', fg='white', bd=5, relief="raised", highlightbackground="black",
                               highlightcolor="black", highlightthickness=2)
        self.btn_signin.place(x=550, y=570, width=200, height=70)

        self.handle_thread_socket()

        # self.protocol("WM_DELETE_WINDOW", self.on_closing)

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

    # def on_closing(self):
    #     if messagebox.askokcancel("Quit", "do you want to close the app?"):
    #         self.send_msg("closed", self.client_socket)
    #         self.running = False
    #         self.destroy()

    def send_msg(self, data, client_socket):
        try:
            print("The message is: " + str(data))
            length = str(len(data)).zfill(SIZE)
            length = length.encode()
            print(length)
            if type(data) != bytes:
                data = data.encode()
            print(data)
            msg = length + data
            print("message with lenght is " + str(msg))
            client_socket.send(msg)
        except Exception as e:
            print("error with sending msg", str(e))
            error_message = "[Errno 32] Broken pipe"
            if str(e) == error_message:
                self.pops_error()
            return None



    def recv_msg(self, client_socket, ret_type="string"):
        try:
            length = client_socket.recv(SIZE).decode(self.format)
            if not length:
                print("no length!")
                return None
            print("The length is " + length)
            data = client_socket.recv(int(length))
            if not data:
                print("no data!")
                return None
            print("the data is: " + str(data))
            if ret_type == "string":
                data = data.decode(self.format)
            print(data)
            return data
        except Exception as e:
            print("error with receiving msg", str(e))
            error_message = "[Errno 54] Connection reset by peer"
            if str(e) == error_message:
                self.pops_error()
            return None

    def pops_error(self):
        messagebox.showerror("connection error", "the server has disconnected.\nplease reconnect later")
        # login_window = Login(self)
        # login_window.grab_set()
        # self.withdraw()
        self.grab_release()  # Release the grab on the current window
        self.withdraw()  # Hide the current window
        self.deiconify()  # Bring the main window back into focus


    # Sender
    # def send_msg(self, data, client_socket):
    #     try:
    #         print("the message is: " + str(data))
    #         if type(data) != bytes:
    #             data = data.encode()
    #         length = len(data)
    #         length = struct.pack("!I", length)
    #         msg = length + data
    #         print("message with length is " + str(msg))
    #         client_socket.sendall(msg)
    #     except Exception as e:
    #         print("Error with sending message:", e)
    #
    # # Receiver
    # def recv_msg(self, client_socket, ret_type="string"):
    #     try:
    #         length = client_socket.recv(4)
    #         if not length:
    #             print("no length!")
    #             return None
    #         length, = struct.unpack("!I", length)
    #         print("The length is " + str(length))
    #         data = client_socket.recv(length)
    #         if not data:
    #             print("no data!")
    #             return None
    #         print("the data is: " + str(data))
    #         if ret_type == "string":
    #             data = data.decode(self.format)
    #         print(data)
    #         return data
    #     except:
    #         print("error with receiving msg")

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 1853))
            # data = self.client_socket.recv(1024).decode()

            data = self.recv_msg(self.client_socket)
            print("data"+data)
            print("hi", self.client_socket)
            # Receive the public key from the server
            # public_key_str = self.recv_msg(self.client_socket)
            #
            # # Deserialize the received public key
            # public_key = serialization.load_pem_public_key(public_key_str.encode())

        except:
            print("server not available")
            messagebox.showerror("notification", "Error, server is not connected")

if __name__ == "__main__":
    app = App()
    app.mainloop()
