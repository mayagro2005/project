import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from dbteachers import teachers
from dbstudents import students
from tkmacosx import Button
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Register(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1000x1000')
        self.title('REGISTER WINDOW')
        self.studentdb= students()
        self.teacherdb= teachers()

        self.create_gui()
        # Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)
        Button(self, text='Close', font=("Helvetica", 16, "bold"), bg='red', fg='white', bd=5, relief=SUNKEN,
               command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        self.lbl_signin = Label(self, text="SIGN UP", font=("Arial", 20, "bold"), background="#f2f2f2", relief=SUNKEN)
        self.lbl_signin.pack(pady=10)

        self.lbl_recognize = Label(self, text="Are you a teacher or student?", font=("Helvetica", 14))
        self.lbl_recognize.pack(pady=10)

        self.var = StringVar()
        self.var.set("teacher")

        self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher",
                                               font=("Helvetica", 14))
        self.teacher_radiobutton.pack(pady=5)

        self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student",
                                               font=("Helvetica", 14))
        self.student_radiobutton.pack(pady=5)

        # Labels and Entries for first name, last name, email, and password
        self.firstname_label = Label(self, text="First Name:", font=("Helvetica", 14))
        self.firstname_label.pack(pady=5)
        self.firstname = Entry(self, font=("Helvetica", 14))
        self.firstname.pack(pady=5)

        self.lastname_label = Label(self, text="Last Name:", font=("Helvetica", 14))
        self.lastname_label.pack(pady=5)
        self.lastname = Entry(self, font=("Helvetica", 14))
        self.lastname.pack(pady=5)

        self.email_label = Label(self, text="Email:", font=("Helvetica", 14))
        self.email_label.pack(pady=5)
        self.email = Entry(self, font=("Helvetica", 14))
        self.email.pack(pady=5)

        self.password_label = Label(self, text="Password:", font=("Helvetica", 14))
        self.password_label.pack(pady=5)
        self.password = Entry(self, font=("Helvetica", 14), show="*")
        self.password.pack(pady=5)

        # Sign In button
        self.sign_in_button = Button(self, text="Sign In", font=("Helvetica", 16), background="white", relief="solid",
                                     borderwidth=2, command=self.handle_add_user)
        self.sign_in_button.pack(pady=20)

        # Login message
        self.str = StringVar()
        self.str.set("")
        self.login_message = Label(self, textvariable=self.str, foreground="red", font=("Helvetica", 14))
        self.login_message.pack(pady=20)





        # self.lbl_recognize = Label(self, width=20, text="Are you teacher or student? ")
        # self.lbl_recognize.place(x=10, y=50)
        # # self.recognize = Entry(self, width=20)
        # # self.recognize.place(x=200, y=50)
        # self.var = StringVar()
        # self.var.set("teacher")
        #
        # self.message_label = None
        #
        #
        # self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher")
        # self.teacher_radiobutton.place(x=200, y=50)
        #
        # self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student")
        # self.student_radiobutton.place(x=290, y=50)
        #
        # # phase 1 button
        # self.lbl_firstname = Label(self, width=10, text="first name :")
        # self.lbl_firstname.place(x=10, y=100)
        # self.firstname = Entry(self, width=20)
        # self.firstname.place(x=150, y=100)
        #
        # self.lbl_lastname = Label(self, width=10, text="last name :")
        # self.lbl_lastname.place(x=10, y=150)
        # self.lastname = Entry(self, width=20)
        # self.lastname.place(x=150, y=150)
        #
        # self.lbl_email = Label(self, width=10, text="email :")
        # self.lbl_email.place(x=10, y=200)
        # self.email = Entry(self, width=20)
        # self.email.place(x=150, y=200)
        #
        # self.lbl_password = Label(self, width=10, text="password :")
        # self.lbl_password.place(x=10, y=250)
        # self.password = Entry(self, width=20)
        # self.password.place(x=150, y=250)
        #
        # self.buttonPlus = Button(self, text="Sign Up", command=self.handle_add_user, width=60, background="white")
        # self.buttonPlus.place(x=50, y=350)
        #
        # self.str = StringVar()
        # self.str.set("")
        # self.labellogin = Label(self, textvariable=self.str, foreground="red")
        # self.labellogin.place(x=200, y=450)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.register_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def register_user(self):
        try:
            if self.var.get() == "teacher":
                if len(self.email.get()) == 0 or len(self.password.get()) == 0 or len(self.firstname.get()) == 0 or len(
                        self.lastname.get()) == 0:
                    messagebox.showerror("please write details", "Error")
                    return
                print("SignUp")
                arr = ["SignUp", "teacher", self.firstname.get(), self.lastname.get(), self.email.get(),
                       self.password.get()]
                str_insert = ",".join(arr)
                print(str_insert)
                self.parent.send_msg(str_insert, self.parent.client_socket)
                data = self.parent.recv_msg(self.parent.client_socket)
                print(data)
                if data == "success register":
                    message = "you signed up, please go to sign in"
                    self.str.set(message)
                    print(self.str.get())
                    # self.message_label.config(text = "you signed up, please go to sign in", foreground = "red")

                elif data == "failed register":
                    # self.message_label.config(text="register failed, try again", foreground="red")
                    message = "register failed, try again"
                    self.str.set(message)
                    print(self.str.get())
                elif data == "exist":
                    message = "you already have a user, go sign in"
                    self.str.set(message)
                    print(self.str.get())
                    # self.message_label.config(text="you already have a user, go sign in", foreground="red")


            elif self.var.get() == "student":
                self.priceforayear = str(0)
                if len(self.email.get()) == 0 or len(self.password.get()) == 0 or len(self.firstname.get()) == 0 or len(
                        self.lastname.get()) == 0:
                    messagebox.showerror("please write details", "Error")
                    return
                print("SignUp")
                arr = ["SignUp", "student", self.firstname.get(), self.lastname.get(), self.priceforayear,
                       self.email.get(),
                       self.password.get()]
                str_insert = ",".join(arr)
                print(str_insert)
                self.parent.send_msg(str_insert, self.parent.client_socket)
                data = self.parent.recv_msg(self.parent.client_socket)
                print(data)
                if data == "exist":
                    # self.message_label.config(text="you signed up, please go to sign in", foreground="red")
                    message = "you already have a user, go sign in"
                    self.str.set(message)
                    print(self.str.get())
                elif data == "success register":
                    # self.message_label.config(text="register failed, try again", foreground="red")
                    message = "you signed up, please go to sign in"
                    self.str.set(message)
                    print(self.str.get())
                    "success register"
                elif data == "failed register":
                    message = "register failed, try again"
                    self.str.set(message)
                    print(self.str.get())
                    # self.message_label.config(text="you already have a user, go sign in", foreground="red")
            else:
                tkinter.messagebox.showerror("error", "SIGN UP AS A TEACHER OR STUDENT!")
                # print("function failed")
                # return "failed"
        except:
            return False










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
