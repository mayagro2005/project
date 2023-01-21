import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from dbteachers import teachers
from dbstudents import students
from menuwindowforteacher import menu
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Login(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1000x1000')
        self.title('LOGIN WINDOW')
        self.studentdb = students()
        self.teacherdb = teachers()

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        self.lbl_recognize = Label(self, width=20, text="Are you teacher or student? ")
        self.lbl_recognize.place(x=10, y=50)
        self.recognize = Entry(self, width=20)
        self.recognize.place(x=200, y=50)
        # phase 1 button
        self.lbl_firstname = Label(self, width=10, text="firstname :")
        self.lbl_firstname.place(x=10, y=100)
        self.firstname = Entry(self, width=20)
        self.firstname.place(x=150, y=100)

        self.lbl_lastname = Label(self, width=10, text="lastname :")
        self.lbl_lastname.place(x=10, y=150)
        self.lastname = Entry(self, width=20)
        self.lastname.place(x=150, y=150)

        self.lbl_email = Label(self, width=10, text="email :")
        self.lbl_email.place(x=10, y=200)
        self.email = Entry(self, width=20)
        self.email.place(x=150, y=200)

        self.lbl_password = Label(self, width=10, text="password :")
        self.lbl_password.place(x=10, y=250)
        self.password = Entry(self, width=20)
        self.password.place(x=150, y=250)

        self.buttonPlus = Button(self, text="Sign In", command=self.handle_add_user, width=20, background="green")
        self.buttonPlus.place(x=10, y=350)

        self.str = StringVar()
        self.str.set("")
        self.labellogin = Label(self, textvariable=self.str, background="light blue")
        self.labellogin.place(x=200, y=450)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.signin_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()



    def signin_user(self):
        if self.recognize.get() == "teacher":
            if len(self.email.get()) == 0 or len(self.password.get()) == 0 or len(self.firstname.get()) == 0 or len(
                    self.lastname.get()) == 0:
                messagebox.showerror("please write details", "Error")
                return
            print("SignIn")
            arr = ["SignIn", "teacher", self.firstname.get(), self.lastname.get(), self.email.get(),
                   self.password.get()]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.client_socket.send(str_insert.encode())
            data = self.parent.client_socket.recv(1024).decode()
            print(data)
            if data != "exist":
                message = "please register"
                self.str.set(message)
                print(self.str.get())

            # if self.teacherdb.insert_teacher(self.firstname.get(), self.lastname.get(), self.email.get(), self.password.get()) != "exist":
            #     message = "please register"
            #     self.str.set(message)
            #     print(self.str.get())
            else:
                window = menu(self, self.firstname.get(), self.lastname.get())
                window.grab_set()
                self.withdraw()
                # message2 = "welcome, you are loged"
                # self.str.set(message2)
                # print(self.str.get())

            # arr = ["SignIn", "teacher", self.firstname.get(), self.lastname.get(), self.email.get(),
            #        self.password.get()]
            # str_insert = ",".join(arr)
            # print(str_insert)
            # self.parent.client_socket.send(str_insert.encode())
            # data = self.parent.client_socket.recv(1024).decode()
            # print(data)
        elif self.recognize.get() == "student":
            self.priceforayear = str(250)
            if len(self.email.get()) == 0 or len(self.password.get()) == 0 or len(self.firstname.get()) == 0 or len(
                    self.lastname.get()) == 0:
                messagebox.showerror("please write details", "Error")
                return
            print("SignIn")
            arr1 = ["SignIn", "student", self.firstname.get(), self.lastname.get(),self.priceforayear, self.email.get(),
                   self.password.get()]
            str_insert = ",".join(arr1)
            print(str_insert)
            self.parent.client_socket.send(str_insert.encode())
            data = self.parent.client_socket.recv(1024).decode()
            print(data)
            if data != "exist":
                message = "please register"
                self.str.set(message)
                print(self.str.get())
            # if self.studentdb.insert_student(self.firstname.get(), self.lastname.get(), self.priceforayear, self.email.get(), self.password.get()) != "exist":
            #     message = "please register"
            #     self.str.set(message)
            #     print(self.str.get())
            else:
                message2 = "welcome, you are loged"
                self.str.set(message2)
                print(self.str.get())
        # Button(self, text='Close', command=self.close).pack(expand=True)
        else:
            tkinter.messagebox.showerror("error", "SIGN IN AS A TEACHER OR STUDENT!")
            # print("function failed")
            # return "failed"

    def close(self):
        self.parent.deiconify()
        self.destroy()