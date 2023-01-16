import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from dbteachers import teachers
from dbstudents import students
import socket
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class menu(tkinter.Toplevel):
    def __init__(self, parent, firstname, lastname):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1000x1000')
        self.title('add user/register')
        self.studentdb= students()
        self.teacherdb= teachers()
        self.firstname = firstname
        self.lastname = lastname

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)

    def create_gui(self):
        self.lbl_welcome = Label(self, width=20, text="Welcome " + self.firstname + " " + self.lastname + " ", background="pink", foreground="black", font=("Calibri",15))
        self.lbl_welcome.place(x=450, y=50, width=140, height=50)
        # self.recognize = Entry(self, width=20)
        # self.recognize.place(x=200, y=50)
        # phase 1 button
    #     self.lbl_firstname = Label(self, width=10, text="firstname :")
    #     self.lbl_firstname.place(x=10, y=100)
    #     self.firstname = Entry(self, width=20)
    #     self.firstname.place(x=150, y=100)
    #
    #     self.lbl_lastname = Label(self, width=10, text="lastname :")
    #     self.lbl_lastname.place(x=10, y=150)
    #     self.lastname = Entry(self, width=20)
    #     self.lastname.place(x=150, y=150)
    #
    #     self.lbl_email = Label(self, width=10, text="email :")
    #     self.lbl_email.place(x=10, y=200)
    #     self.email = Entry(self, width=20)
    #     self.email.place(x=150, y=200)
    #
    #     self.lbl_password = Label(self, width=10, text="password :")
    #     self.lbl_password.place(x=10, y=250)
    #     self.password = Entry(self, width=20)
    #     self.password.place(x=150, y=250)
    #

        self.buttondeletelesson = Button(self, text="DELETE LESSON", command=self.delete_lesson, width=20,height=30)
        self.buttondeletelesson.place(x=700, y=150)

        self.buttoninsertlesson = Button(self, text="INSERT LESSON", command=self.insert_lesson, width=20, height=30)
        self.buttoninsertlesson.place(x=50, y=150)

        self.buttonpayment = Button(self, text="PAYMENT BOX", command=self.payment_box, width=20,height=30)
        self.buttonpayment.place(x=50, y=250)

        self.buttonmessages = Button(self, text="MESSAGE BOX", command=self.message_box, width=20,height=30)
        self.buttonmessages.place(x=700, y=250)

    def insert_lesson(self):
        pass
    def delete_lesson(self):
        pass
    def payment_box(self):
        pass
    def message_box(self):
        pass



    #
    # def handle_add_user(self):
    #     self.client_handler = threading.Thread(target=self.register_user, args=())
    #     self.client_handler.daemon = True
    #     self.client_handler.start()
    #
    # def register_user(self):
    #     if self.recognize.get() == "teacher":
    #         if len(self.email.get()) == 0 or len(self.password.get()) == 0 or len(self.firstname.get()) == 0 or len(self.lastname.get()) == 0:
    #             messagebox.showerror("please write details", "Error")
    #             return
    #         print("SignUp")
    #         arr = ["SignUp", "teacher", self.firstname.get(), self.lastname.get(), self.email.get(), self.password.get()]
    #         str_insert = ",".join(arr)
    #         print(str_insert)
    #         self.parent.client_socket.send(str_insert.encode())
    #         data = self.parent.client_socket.recv(1024).decode()
    #         print(data)
    #     else:
    #         self.priceforayear = int(250)
    #         if len(self.email.get()) == 0 or len(self.password.get()) == 0 or len(self.firstname.get()) == 0 or len(self.lastname.get()) == 0:
    #             messagebox.showerror("please write details", "Error")
    #             return
    #         print("SignUp")
    #         arr = ["SignUp", "student", self.firstname.get(), self.lastname.get(), self.priceforayear, self.email.get(),
    #                self.password.get()]
    #         str_insert = ",".join(arr)
    #         print(str_insert)
    #         self.parent.client_socket.send(str_insert.encode())
    #         data = self.parent.client_socket.recv(1024).decode()
    #         print(data)









        # if len(self.email.get())==0 and len(self.password.get()) == 0:
        #     messagebox.showerror("please write details", "Error")
        #     return
        # print("register")
        # arr = ["register", self.email.get(), self.password.get(), self.firstname.get()]
        # str_insert = ",".join(arr)
        # print(str_insert)
        # self.parent.client_socket.send(str_insert.encode())
        # data = self.parent.client_socket.recv(1024).decode()
        # print(data)

    # old register user
    # def register_user(self):
    #     if len(self.email.get())==0:
    #         messagebox.showerror("please write city name", "Error")
    #         return
    #     self.userdb.insert_user(self.email.get(), self.password.get(), self.firstname.get())
    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen
