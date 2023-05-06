import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import socket
from rgb import rgbprint
from tkmacosx import Button
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
# class Messages_for_student(tkinter.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#         self.geometry('500x500')
#         self.title('MESSAGE BOX')
#         self.create_gui()
#         # Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)
#         Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
#         # self.close_button = Button(self, text='Close', command=self.close)
#         # self.close_button.grid(row=100, column=0, sticky='s')
#
#     def create_gui(self):
#         self.lbl_welcome = Label(self, text="Hello! this is your message box ",background="light blue", foreground="black", font=("Calibri",14))
#         self.lbl_welcome.place(x=160, y=20)
#         self.lbl_chooseperson = Label(self, text="choose for who to write the message: ")
#         self.lbl_chooseperson.place(x=120, y=220)
#         # self.recognize = Entry(self, width=20)
#         # self.recognize.place(x=200, y=50)
#         self.var = StringVar()
#         self.var.set("teacher")
#
#         self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher",
#                                                font=("Helvetica", 14))
#         self.teacher_radiobutton.place(x=170,y=250)
#
#         self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student",
#                                                font=("Helvetica", 14))
#         self.student_radiobutton.place(x=170,y=270)
#         self.nameofperson_var = StringVar()
#         if self.var.get() == "teacher":
#             self.parent.parent.parent.send_msg("Teacher List", self.parent.parent.parent.client_socket)
#             data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
#             arr = data.split(",")
#             arr.insert(0, "all teachers")
#             self.nameofperson = OptionMenu(self, self.nameofperson_var, *arr)
#             self.nameofperson.config(font=("Helvetica", 14), width=20)
#             self.nameofperson.place(x=170,y=300)
#         elif self.var.get() == "student":
#             self.parent.parent.parent.send_msg("Student List", self.parent.parent.parent.client_socket)
#             data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
#             arr1 = data.split(",")
#             arr1.insert(0, "all students")
#             self.nameofperson = OptionMenu(self, self.nameofperson_var, *arr1)
#             self.nameofperson.config(font=("Helvetica", 14), width=20)
#             self.nameofperson.place(x=170, y=300)
#         self.lbl_writemessage = Label(self, text="write a message: ")
#         self.lbl_writemessage.place(x=50, y=400)
#         self.writemessage = Entry(self, width=20)
#         self.writemessage.place(x=290, y=400)
#         self.send_message_button = Button(self, text='Send', command=self.handle_send_message)
#         self.send_message_button.place(x=190,y=430)
#         self.message_label = Entry(self, width=30,foreground="red")
#         self.message_label.place(x=120,y=100)
#         self.message_label.insert(0, "received messages")
#         self.message_label.config(state='readonly')
#         self.message_label = StringVar()
class Messages_for_student(tkinter.Toplevel):
    def __init__(self, parent, firstname, lastname,teacher_or_student):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x500')
        self.title('MESSAGE BOX')
        self.firstname = firstname
        self.lastname = lastname
        self.teacher_or_student = teacher_or_student
        self.config(bg="#AFD3E2")
        self.create_gui()
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)

    def create_gui(self):
        self.lbl_welcome = Label(self, text="Hello! this is your message box ",background="light blue", foreground="black", font=("Calibri",14))
        self.lbl_welcome.place(x=160, y=20)

        self.lbl_chooseperson = Label(self, text="choose for who to write the message: ")
        self.lbl_chooseperson.place(x=120, y=220)

        self.var = StringVar()
        self.var.set("teacher")

        self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher",
                                               font=("Helvetica", 14), command=self.update_options)
        self.teacher_radiobutton.place(x=170,y=250)

        self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student",
                                               font=("Helvetica", 14), command=self.update_options)
        self.student_radiobutton.place(x=170,y=280)

        self.nameofperson_var = StringVar()

        self.parent.parent.parent.send_msg("Teacher List", self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        self.teacher_list = data.split(",")

        self.parent.parent.parent.send_msg("Student List", self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        self.student_list = data.split(",")

        self.all_teachers_and_students = ["all teachers"] + self.teacher_list + ["all students"] + self.student_list

        self.nameofperson = OptionMenu(self, self.nameofperson_var, *self.all_teachers_and_students)
        self.nameofperson.config(font=("Helvetica", 14), width=20)
        self.nameofperson.place(x=170,y=310)

        self.lbl_writemessage = Label(self, text="write a message: ")
        self.lbl_writemessage.place(x=50, y=400)

        self.writemessage = Entry(self, width=20)
        self.writemessage.place(x=290, y=400)

        self.send_message_button = Button(self, text='Send', command=self.handle_send_message)
        self.send_message_button.place(x=190,y=430)

        self.message_label = Entry(self, width=70,foreground="red")
        self.message_label.place(x=120,y=100)
        self.message_label.insert(0, "received messages")
        self.message_label.config(state='readonly')

    def update_options(self):
        if self.var.get() == "teacher":
            self.nameofperson['menu'].delete(0, 'end')
            for option in self.all_teachers_and_students:
                if option in self.teacher_list or option == "all teachers":
                    self.nameofperson['menu'].add_command(label=option,
                                                          command=lambda value=option: self.nameofperson_var.set(value))
        elif self.var.get() == "student":
            self.nameofperson['menu'].delete(0, 'end')
            for option in self.all_teachers_and_students:
                if option in self.student_list or option == "all students":
                    self.nameofperson['menu'].add_command(label=option,
                                                          command=lambda value=option: self.nameofperson_var.set(value))

    def handle_send_message(self):
        # message = self.writemessage.get()
        # self.parent.server.send_message(message)
        print("Send")
        # arr = ["Send", "Message", f"{self.firstname} {self.lastname}", self.var.get(), self.nameofperson_var.get(),
        #        self.writemessage.get()]
        arr = ["Send", "Message", self.nameofperson_var.get(),self.var.get()
            ,f"{self.firstname} {self.lastname}",self.teacher_or_student,self.writemessage.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        recieved_data = data.split(",")
        print(recieved_data)
        sender = recieved_data[0]
        recipient = recieved_data[1]
        message_text = recieved_data[2]
        if recipient == f"{self.firstname} {self.lastname}" or recipient == "all students":
            message = f"From: {sender}\n\n{message_text}"
            self.handle_received_message(message)
        else:
            pass


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