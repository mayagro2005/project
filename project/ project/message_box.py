import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from dbteachers import teachers
from dbstudents import students
import socket
from rgb import rgbprint
from tkmacosx import Button
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Messages(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x500')
        self.title('MESSAGE BOX')
        self.studentdb= students()
        self.teacherdb= teachers()
        self.create_gui()
        # Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # self.close_button = Button(self, text='Close', command=self.close)
        # self.close_button.grid(row=100, column=0, sticky='s')

    def create_gui(self):
        self.lbl_welcome = Label(self, text="Hello! this is your message box ",background="light blue", foreground="black", font=("Calibri",14))
        self.lbl_welcome.place(x=160, y=20)
        # self.recognize = Entry(self, width=20)
        # self.recognize.place(x=200, y=50)
        self.lbl_writemessage = Label(self, text="write a message for your students: ")
        self.lbl_writemessage.place(x=50, y=400)
        self.writemessage = Entry(self, width=20)
        self.writemessage.place(x=290, y=400)
        self.send_message_button = Button(self, text='Send', command=self.handle_send_message)
        self.send_message_button.place(x=190,y=430)
        self.message_label = Entry(self, width=30,foreground="red")
        self.message_label.place(x=120,y=100)
        self.message_label.insert(0, "received messages")
        self.message_label.config(state='readonly')
        # self.message_label = StringVar()



    def handle_send_message(self):
        # message = self.writemessage.get()
        # self.parent.server.send_message(message)
        print("Send")
        arr = ["Send", "Message", self.writemessage.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        self.handle_received_message(data)

    # def handle_received_message(self, message):
    #     print(message)
    #     self.message_label.delete(0, END)
    #     self.message_label.insert(0,message)
    def handle_received_message(self, message):
        self.update_message_label(message)

    def update_message_label(self, message):
        self.message_label.config(state='normal')
        self.message_label.delete(0, END)
        self.message_label.insert(0, message)
        self.message_label.config(state='readonly')

    def close(self):
        self.parent.deiconify()
        self.destroy()