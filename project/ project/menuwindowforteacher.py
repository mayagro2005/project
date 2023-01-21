import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from dbteachers import teachers
from dbstudents import students
import socket
from rgb import rgbprint
from message_box import Messages
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
        # Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)








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

        self.buttondeletelesson = Button(self, text="DELETE LESSON", command=self.delete_lesson, width=20)
        self.buttondeletelesson.place(x=700, y=150)

        self.buttoninsertlesson = Button(self, text="INSERT LESSON", command=self.insert_lesson, width=20)
        self.buttoninsertlesson.place(x=50, y=150)

        self.buttonpayment = Button(self, text="PAYMENT BOX", command=self.payment_box, width=20)
        self.buttonpayment.place(x=50, y=250)

        self.buttonmessages = Button(self, text="MESSAGE BOX", command=self.message_box, width=20)
        self.buttonmessages.place(x=700, y=250)

        self.btn_kidstennis = Button(self, text='KIDS TENNIS', background="#B5D5C5", foreground="black", font=("Calibri", 15),
                                 command=self.open_tennis)
        self.btn_kidstennis.place(x=120, y=400, width=120, height=120)

        self.btn_swimming = Button(self, text='SWIMMING', background="#B5D5C5", foreground="black", font=("Calibri", 15),
                                 command=self.open_swimming)
        self.btn_swimming.place(x=270, y=400, width=120, height=120)

        self.btn_yoga = Button(self, text='YOGA', background="#5BC0F8", foreground="black", font=("Calibri", 15),
                                   command=self.open_yoga)
        self.btn_yoga.place(x=420, y=400, width=120, height=120)

        self.btn_basketball = Button(self, text='BASKETBALL', background="#ADA2FF", foreground="black", font=("Calibri", 15),
                               command=self.open_basketball)
        self.btn_basketball.place(x=570, y=400, width=120, height=120)

        self.btn_dancing = Button(self, text='DANCING', background="#F8F988", foreground="black",
                                     font=("Calibri", 15),
                                     command=self.open_dancing)
        self.btn_dancing.place(x=720, y=400, width=120, height=120)

        self.btn_adultstennis = Button(self, text='ADULTS TENNIS', background="#DC3535", foreground="black", font=("Calibri", 15),
                                 command=self.open_adultstennis)
        self.btn_adultstennis.place(x=120, y=620, width=120, height=120)

        self.btn_pingpong = Button(self, text='PING PONG', background="#E97777", foreground="black", font=("Calibri", 15),
                                   command=self.open_pingpong)
        self.btn_pingpong.place(x=270, y=620, width=120, height=120)

        self.btn_fitness = Button(self, text='FITNESS', background="#4649FF", foreground="black", font=("Calibri", 15),
                               command=self.open_fitness)
        self.btn_fitness.place(x=420, y=620, width=120, height=120)

        self.btn_pilates = Button(self, text='PILATES', background="#FFF6BF", foreground="black",
                                     font=("Calibri", 15),
                                     command=self.open_pilates)
        self.btn_pilates.place(x=570, y=620, width=120, height=120)

        self.btn_boxing = Button(self, text='BOXING', background="#E8AA42", foreground="black",
                                  font=("Calibri", 15),
                                  command=self.open_boxing)
        self.btn_boxing.place(x=720, y=620, width=120, height=120)

    def insert_lesson(self):
        pass
    def delete_lesson(self):
        pass
    def payment_box(self):
        pass
    def message_box(self):
        window = Messages(self)
        window.grab_set()
        # self.withdraw()
    def open_tennis(self):
        pass
    def open_swimming(self):
        pass
    def open_yoga(self):
        pass
    def open_basketball(self):
        pass
    def open_dancing(self):
        pass
    def open_adultstennis(self):
        pass
    def open_pingpong(self):
        pass
    def open_fitness(self):
        pass
    def open_pilates(self):
        pass
    def open_boxing(self):
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
