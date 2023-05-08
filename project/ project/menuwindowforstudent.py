import threading
import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import ttk, messagebox
import socket
from rgb import rgbprint
from message_box import Messages
from payment_box import Payments
from tkmacosx import Button
from message_box_for_student import Messages_for_student
from insert_lesson_window import insert_lesson
from delete_lesson_window import delete_lesson
from update_lesson_window import update_lesson
from kids_tennis_window_student import kids_tennis_lesson_student
from adults_tennis_window_student import adults_tennis_lesson_student
from basketball_window_student import basketball_lesson_student
from boxing_window_student import boxing_lesson_student
from dance_window_student import dance_lesson_student
from fitness_window_student import fitness_lesson_student
from pilates_window_student import pilates_lesson_student
from ping_pong_window_student import ping_pong_lesson_student
from swimming_window_student import swimming_lesson_student
from yoga_window_student import yoga_lesson_student
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class menuforstudent(tkinter.Toplevel):
    def __init__(self, parent, firstname, lastname, email, password,teacher_or_student):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1000x1000')
        self.title('MAIN WINDOW')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.teacher_or_student = teacher_or_student
        self.config(bg="#FFF8E1")

        self.create_gui()
        # Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)
        # Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
        Button(self, text='GO BACK', font=("Helvetica", 16, "bold"), bg='red', fg='white', bd=5, relief=SUNKEN,
               command=self.close).place(relx=0.5, rely=1.0, anchor='s', height=50, width=100, bordermode='outside')

    def create_gui(self):
        self.lbl_welcome = Label(self, text="Welcome " + self.firstname + " " + self.lastname + " ",
                                 background="#5BC0F8", foreground="white", font=("Montserrat", 25, 'bold'),
                                 relief="solid", bd=5)
        self.lbl_welcome.place(x=0, y=50, width=1000, height=70)
        # self.buttondeletelesson = Button(self, text="DELETE LESSON", background="#ECE8DD", foreground="black",
        #                                  font=("Calibri", 13, 'bold'), command=self.delete_lesson)
        # self.buttondeletelesson.place(x=720, y=150, width=150, height=70)
        #
        # self.buttoninsertlesson = Button(self, text="INSERT LESSON", background="#ECE8DD", foreground="black",
        #                                  font=("Calibri", 13, 'bold'), command=self.insert_lesson)
        # self.buttoninsertlesson.place(x=50, y=150, width=150, height=70)
        #
        self.buttonpaymentbox = Button(self, text="PAYMENT BOX", background="#C0DEFF", foreground="black",
                                         font=("Calibri", 13, 'bold'),relief="solid", bd=3, command=self.payment_box)
        self.buttonpaymentbox.place(x=50, y=150, width=150, height=70)

        self.buttonmessages = Button(self, text="MESSAGE BOX", background="#C0DEFF", foreground="black",
                                     font=("Calibri", 13, 'bold'),relief="solid", bd=3, command=self.message_box)
        self.buttonmessages.place(x=720, y=150, width=150, height=70)

        self.btn_kidstennis = Button(self, text='KIDS TENNIS', bg="#B5D5C5", foreground="white",
                                     font=("Calibri", 15, 'bold'), relief="solid", bd=2,
                                     command=self.open_tennis)
        self.btn_kidstennis.place(x=120, y=400, width=120, height=120)

        self.btn_swimming = Button(self, text='SWIMMING', bg="#FFE9B1", foreground="black",
                                   font=("Calibri", 15, 'bold'), relief="solid", bd=2,
                                   command=self.open_swimming)
        self.btn_swimming.place(x=270, y=400, width=120, height=120)

        self.btn_yoga = Button(self, text='YOGA', background="#FFD4D4", foreground="black",
                               font=("Calibri", 15, 'bold'), relief="solid", bd=2,
                               command=self.open_yoga)
        self.btn_yoga.place(x=420, y=400, width=120, height=120)

        self.btn_basketball = Button(self, text='BASKETBALL', background="#ADA2FF", foreground="white", relief="solid",
                                     bd=2,
                                     font=("Calibri", 15, 'bold'),
                                     command=self.open_basketball)
        self.btn_basketball.place(x=570, y=400, width=120, height=120)

        self.btn_dancing = Button(self, text='DANCING', background="#F8F988", foreground="black", relief="solid", bd=2,
                                  font=("Calibri", 15, 'bold'),
                                  command=self.open_dancing)
        self.btn_dancing.place(x=720, y=400, width=120, height=120)

        self.btn_adultstennis = Button(self, text='ADULTS TENNIS', background="#91D8E4", foreground="black",
                                       relief="solid", bd=2,
                                       font=("Calibri", 15, 'bold'),
                                       command=self.open_adultstennis)
        self.btn_adultstennis.place(x=120, y=620, width=120, height=120)

        self.btn_pingpong = Button(self, text='PING PONG', background="#82AAE3", foreground="black", relief="solid",
                                   bd=2,
                                   font=("Calibri", 15, 'bold'),
                                   command=self.open_pingpong)
        self.btn_pingpong.place(x=270, y=620, width=120, height=120)

        self.btn_fitness = Button(self, text='FITNESS', background="#B5D5C5", foreground="black",
                                  font=("Calibri", 15, 'bold'), relief="solid", bd=2,
                                  command=self.open_fitness)
        self.btn_fitness.place(x=420, y=620, width=120, height=120)

        self.btn_pilates = Button(self, text='PILATES', background="#FFF6BF", foreground="black", relief="solid", bd=2,
                                  font=("Calibri", 15, 'bold'),
                                  command=self.open_pilates)
        self.btn_pilates.place(x=570, y=620, width=120, height=120)

        self.btn_boxing = Button(self, text='BOXING', background="#FFE1E1", foreground="black", relief="solid", bd=2,
                                 font=("Calibri", 15, 'bold'),
                                 command=self.open_boxing)
        self.btn_boxing.place(x=720, y=620, width=120, height=120)

    # def insert_lesson(self):
    #     window = insert_lesson(self,self.email,self.password)
    #     window.grab_set()
    # def delete_lesson(self):
    #     window = delete_lesson(self, self.email, self.password)
    #     window.grab_set()
    def payment_box(self):
        window = Payments(self, self.email, self.password)
        window.grab_set()
    # def updatelesson(self):
    #     window = update_lesson(self, self.email, self.password)
    #     window.grab_set()
    def message_box(self):
        window = Messages_for_student(self, self.firstname, self.lastname, self.teacher_or_student)
        window.grab_set()
        # self.withdraw()

    def open_tennis(self):
        window = kids_tennis_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_swimming(self):
        window = swimming_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_yoga(self):
        window = yoga_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_basketball(self):
        window = basketball_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_dancing(self):
        window = dance_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_adultstennis(self):
        window = adults_tennis_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_pingpong(self):
        window = ping_pong_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_fitness(self):
        window = fitness_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_pilates(self):
        window = pilates_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()
    def open_boxing(self):
        window = boxing_lesson_student(self, self.firstname, self.lastname)
        window.grab_set()









    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen
