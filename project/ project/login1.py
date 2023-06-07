import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
# from dbteachers import teachers
# from dbstudents import students
from PIL import ImageTk, Image
from menuwindowforteacher import menu
from tkmacosx import Button
from menuwindowforstudent import menuforstudent
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Login(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('447x667')
        self.title('LOGIN WINDOW')
        self.img = Image.open('playertennis.png')
        self.resized = self.img.resize((447, 667), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.label_image = Label(self, image=self.image)
        self.label_image.place(x=0, y=0)

        self.create_gui()
        Button(self, text='Close', font=("Helvetica", 16, "bold"), bg='red', fg='white', bd=5, relief=SUNKEN,
               command=self.close).pack(expand=True, side=BOTTOM)

        # Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):

        # self.canvas = Canvas(self, width=447, height=667,bd=0,highlightthickness=0)
        # self.canvas.pack()
        # self.img = Image.open('playertennis.png')
        # self.resized = self.img.resize((447, 667), Image.LANCZOS)
        # self.image = ImageTk.PhotoImage(self.resized)
        # self.photo = self.canvas.create_image(0,0,anchor=NW, image = self.image)

        self.lbl_signin = Label(self, text="SIGN IN", font=("Arial", 20, "bold"), relief=SUNKEN)
        self.lbl_signin.pack(pady=10)


        self.lbl_recognize = Label(self, text="Are you a teacher or student?", font=("Arial", 16, "bold"), background="#f2f2f2", relief=SUNKEN)
        self.lbl_recognize.pack(pady=10)

        self.var = StringVar()
        self.var.set("teacher")

        self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher",
                                               font=("Arial", 14, "bold"), background="#f2f2f2", relief=SUNKEN)
        self.teacher_radiobutton.pack(pady=5)

        self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student",
                                               font=("Arial", 14, "bold"), background="#f2f2f2", relief=SUNKEN)
        self.student_radiobutton.pack(pady=5)

        # Labels and Entries for first name, last name, email, and password
        # self.firstname_label = Label(self, text="First Name:", font=("Helvetica", 14))
        # self.firstname_label.pack(pady=5)
        # self.firstname = Entry(self, font=("Helvetica", 14))
        # self.firstname.pack(pady=5)
        #
        # self.lastname_label = Label(self, text="Last Name:", font=("Helvetica", 14))
        # self.lastname_label.pack(pady=5)
        # self.lastname = Entry(self, font=("Helvetica", 14))
        # self.lastname.pack(pady=5)

        self.email_label = Label(self, text="Email:", font=("Arial", 16, "bold"), background="#f2f2f2", relief=SUNKEN)
        self.email_label.pack(pady=5)
        self.email = Entry(self, font=("Arial", 16, "bold"), relief=SUNKEN)
        self.email.pack(pady=5)

        self.password_label = Label(self, text="Password:", font=("Arial", 16, "bold"), background="#f2f2f2", relief=SUNKEN)
        self.password_label.pack(pady=5)
        self.password = Entry(self, font=("Arial", 16, "bold"), relief=SUNKEN, show="*")
        self.password.pack(pady=5)

        # Sign In button
        self.sign_in_button = Button(self, text="Sign In", font=("Helvetica", 16), background="white", relief="solid",
                                     borderwidth=2,command=self.handle_add_user)
        self.sign_in_button.pack(pady=20)

        # Login message
        self.str = StringVar()
        self.str.set("")
        self.login_message = Label(self, textvariable=self.str, foreground="red", font=("Helvetica", 14))
        self.login_message.pack(pady=20)
        self.login_message.pack_forget()
        # self.lbl_recognize = Label(self, width=20, text="Are you teacher or student? ")
        # self.lbl_recognize.place(x=10, y=50)
        # self.recognize = Entry(self, width=20)
        # self.recognize.place(x=200, y=50)
        # self.lbl_recognize = Label(self, text="Are you a teacher or student?")
        # self.lbl_recognize.place(x=10, y=50)
        #
        # self.var = StringVar()
        # self.var.set("teacher")
        #
        # self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher")
        # self.teacher_radiobutton.place(x=200, y=50)
        #
        # self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student")
        # self.student_radiobutton.place(x=290, y=50)
        #
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
        # self.buttonPlus = Button(self, text="Sign In", command=self.handle_add_user, width=60, background="white")
        # self.buttonPlus.place(x=50, y=350)
        #
        # self.str = StringVar()
        # self.str.set("")
        # self.labellogin = Label(self, textvariable=self.str, foreground="red")
        # self.labellogin.place(x=200, y=450)


    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.signin_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()



    def signin_user(self):
        try:
            if self.var.get() == "teacher":
                if len(self.email.get()) == 0 or len(self.password.get()) == 0:
                    messagebox.showerror("please write details", "Error")
                    return
                print("SignIn")
                arr = ["SignIn", "teacher", self.email.get(),
                       self.password.get()]
                str_insert = ",".join(arr)
                print(str_insert)
                self.parent.send_msg(str_insert, self.parent.client_socket)
                data = self.parent.recv_msg(self.parent.client_socket)
                print(data)
                if data != "exist":
                    message = "please register"
                    self.str.set(message)
                    print(self.str.get())
                    self.login_message.pack()

                # if self.teacherdb.insert_teacher(self.firstname.get(), self.lastname.get(), self.email.get(), self.password.get()) != "exist":
                #     message = "please register"
                #     self.str.set(message)
                #     print(self.str.get())
                else:
                    arr = ["get teacher name", self.email.get(), self.password.get()]
                    str_names = ",".join(arr)
                    print(str_names)
                    self.parent.send_msg(str_names, self.parent.client_socket)
                    names = self.parent.recv_msg(self.parent.client_socket)
                    names = names.split(",")
                    print(names)
                    window = menu(self, names[0], names[1], self.email.get(), self.password.get(),self.var.get())
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
            elif self.var.get() == "student":
                self.priceforayear = str(0)
                if len(self.email.get()) == 0 or len(self.password.get()) == 0:
                    messagebox.showerror("please write details", "Error")
                    return
                print("SignIn")
                arr1 = ["SignIn", "student",
                        self.email.get(),
                        self.password.get()]
                str_insert = ",".join(arr1)
                print(str_insert)
                self.parent.send_msg(str_insert, self.parent.client_socket)
                data = self.parent.recv_msg(self.parent.client_socket)
                print(data)
                if data != "exist":
                    message = "please register"
                    self.str.set(message)
                    print(self.str.get())
                    self.login_message.pack()
                # if self.studentdb.insert_student(self.firstname.get(), self.lastname.get(), self.priceforayear, self.email.get(), self.password.get()) != "exist":
                #     message = "please register"
                #     self.str.set(message)
                #     print(self.str.get())
                else:
                    arr = ["get student name", self.email.get(), self.password.get()]
                    str_names = ",".join(arr)
                    print(str_names)
                    self.parent.send_msg(str_names, self.parent.client_socket)
                    names = self.parent.recv_msg(self.parent.client_socket)
                    names = names.split(",")
                    print(names)
                    window = menuforstudent(self, names[0], names[1], self.email.get(),
                                  self.password.get(),self.var.get())
                    window.grab_set()
                    self.withdraw()
            # Button(self, text='Close', command=self.close).pack(expand=True)
            else:
                tkinter.messagebox.showerror("error", "SIGN IN AS A TEACHER OR STUDENT!")
                # print("function failed")
                # return "failed"
        except:
            return False


    def close(self):
        self.parent.deiconify()
        self.destroy()