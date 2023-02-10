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
from insert_lesson_window import insert_lesson
from delete_lesson_window import delete_lesson
from update_lesson_window import update_lesson
from kids_tennis_window import tennis_lesson
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class menu(tkinter.Toplevel):
    def __init__(self, parent, firstname, lastname, email, password):
        super().__init__(parent)
        self.parent = parent
        self.geometry('1000x1000')
        self.title('MAIN WINDOW')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.kids_tennis_window = None

        self.create_gui()
        # Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)

    def create_gui(self):

        self.lbl_welcome = Label(self, text="Welcome " + self.firstname + " " + self.lastname + " ",
                                 background="#5BC0F8", foreground="white", font=("Montserrat", 25, 'bold'),
                                 highlightcolor="red", relief="solid", bd=5)
        self.lbl_welcome.place(x=300, y=50, width=380, height=70)

        self.buttondeletelesson = Button(self, text="DELETE LESSON", background="#ECE8DD", foreground="black",
                                         font=("Calibri", 13, 'bold'), command=self.delete_lesson)
        self.buttondeletelesson.place(x=720, y=150, width=150, height=70)

        self.buttoninsertlesson = Button(self, text="INSERT LESSON", background="#ECE8DD", foreground="black",
                                         font=("Calibri", 13, 'bold'), command=self.insert_lesson)
        self.buttoninsertlesson.place(x=50, y=150, width=150, height=70)

        self.buttonupdatelesson = Button(self, text="UPDATE LESSON", background="#ECE8DD", foreground="black",
                                         font=("Calibri", 13, 'bold'), command=self.updatelesson)
        self.buttonupdatelesson.place(x=50, y=250, width=150, height=70)

        self.buttonmessages = Button(self, text="MESSAGE BOX", background="#ECE8DD", foreground="black",
                                     font=("Calibri", 13, 'bold'), command=self.message_box)
        self.buttonmessages.place(x=720, y=250, width=150, height=70)

        self.btn_kidstennis = Button(self, text='KIDS TENNIS', bg="#B5D5C5", foreground="white", font=("Calibri", 15),
                                     command=self.open_tennis)
        self.btn_kidstennis.place(x=120, y=400, width=120, height=120)

        self.btn_swimming = Button(self, text='SWIMMING', bg="#FFE9B1", foreground="black", font=("Calibri", 15),
                                   command=self.open_swimming)
        self.btn_swimming.place(x=270, y=400, width=120, height=120)

        self.btn_yoga = Button(self, text='YOGA', background="#FFD4D4", foreground="black", font=("Calibri", 15),
                               command=self.open_yoga)
        self.btn_yoga.place(x=420, y=400, width=120, height=120)

        self.btn_basketball = Button(self, text='BASKETBALL', background="#ADA2FF", foreground="white",
                                     font=("Calibri", 15),
                                     command=self.open_basketball)
        self.btn_basketball.place(x=570, y=400, width=120, height=120)

        self.btn_dancing = Button(self, text='DANCING', background="#F8F988", foreground="black",
                                  font=("Calibri", 15),
                                  command=self.open_dancing)
        self.btn_dancing.place(x=720, y=400, width=120, height=120)

        self.btn_adultstennis = Button(self, text='ADULTS TENNIS', background="#91D8E4", foreground="black",
                                       font=("Calibri", 15),
                                       command=self.open_adultstennis)
        self.btn_adultstennis.place(x=120, y=620, width=120, height=120)

        self.btn_pingpong = Button(self, text='PING PONG', background="#82AAE3", foreground="black",
                                   font=("Calibri", 15),
                                   command=self.open_pingpong)
        self.btn_pingpong.place(x=270, y=620, width=120, height=120)

        self.btn_fitness = Button(self, text='FITNESS', background="#B5D5C5", foreground="black", font=("Calibri", 15),
                                  command=self.open_fitness)
        self.btn_fitness.place(x=420, y=620, width=120, height=120)

        self.btn_pilates = Button(self, text='PILATES', background="#FFF6BF", foreground="black",
                                  font=("Calibri", 15),
                                  command=self.open_pilates)
        self.btn_pilates.place(x=570, y=620, width=120, height=120)

        self.btn_boxing = Button(self, text='BOXING', background="#FFE1E1", foreground="black",
                                 font=("Calibri", 15),
                                 command=self.open_boxing)
        self.btn_boxing.place(x=720, y=620, width=120, height=120)

    def insert_lesson(self):
        window = insert_lesson(self,self.email,self.password)
        window.grab_set()
    def delete_lesson(self):
        window = delete_lesson(self, self.email, self.password)
        window.grab_set()
    # def payment_box(self):
    #     window = Payments(self)
    #     window.grab_set()
    def updatelesson(self):
        window = update_lesson(self, self.email, self.password)
        window.grab_set()
    def message_box(self):
        window = Messages(self)
        window.grab_set()
        # self.withdraw()

    def open_tennis(self):
        window = tennis_lesson(self)
        window.grab_set()
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









    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen
