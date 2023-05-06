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
class Messages(tkinter.Toplevel):
    def __init__(self, parent, firstname, lastname,teacher_or_student):
        super().__init__(parent)
        self.parent = parent
        self.geometry('700x650')
        self.title('MESSAGE BOX')
        self.firstname = firstname
        self.lastname = lastname
        self.teacher_or_student = teacher_or_student
        self.config(bg="#AFD3E2")
        self.create_gui()
        # Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
        Button(self, text='Close', font=("Helvetica", 12, "bold"), command=self.close).pack(side=tkinter.BOTTOM,
                                                                                            fill=tkinter.X)

    def create_gui(self):
        self.lbl_welcome = Label(self, text="Hello! This is your message box ", bg="#19A7CE", fg="black",
                                 font=("Arial", 20, "bold"),relief="solid", bd=3)
        self.lbl_welcome.place(x=200, y=20)

        self.lbl_chooseperson = Label(self, text="Choose who to write the message for: ", font=("Arial", 14, "bold"),relief="solid", bd=3)
        self.lbl_chooseperson.place(x=220, y=60)

        self.var = StringVar()
        self.var.set("teacher")

        self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher",
                                               font=("Helvetica", 14),relief="solid", bd=3, command=self.update_options)
        self.teacher_radiobutton.place(x=300, y=90)

        self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student",
                                               font=("Helvetica", 14),relief="solid", bd=3, command=self.update_options)
        self.student_radiobutton.place(x=300, y=120)

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
        self.nameofperson.place(x=300, y=150)

        self.lbl_writemessage = Label(self, text="Write a message: ", font=("Arial", 14, "bold"),relief="solid", bd=3)
        self.lbl_writemessage.place(x=50, y=550)

        self.writemessage = Entry(self, width=20)
        self.writemessage.place(x=260, y=550)

        self.send_message_button = Button(self, text='Send', command=self.handle_send_message)
        self.send_message_button.place(x=190, y=580)

        self.message_box_label = Label(self, text="Received messages:", bg="#19A7CE", fg="black",
                               font=("Arial", 16, "bold"),relief="solid", bd=3)
        self.message_box_label.place(x=50, y=170)

        self.message_box = Text(self, height=20, width=50, state='disabled', font=("Calibri", 12),relief="solid", bd=3)
        self.message_box.place(x=90, y=210)
        self.message_box.configure(state='normal')
        # self.message_box.insert('end', "No messages received yet.\n")
        self.message_box.configure(state='disabled')
        self.get_message()

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
        if data == "sent":
            messagebox.showinfo("notification", "message was sent successfully")
        elif data == "failed":
            messagebox.showinfo("notification", "sending message failed, try again")

    def get_message(self):
        print("get messages")
        arr = ["get messages", f"{self.firstname} {self.lastname}", self.teacher_or_student]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        if data is not None and data != '':
            arr = data.split("*")
            messages = []
            for el in arr:
                element = el.split(",")
                messages.append(f"from: {element[0]}, {element[1]}, the message: {element[2]}")
            self.message_box.configure(state='normal')
            self.message_box.delete('1.0', 'end')
            self.message_box.insert('end', '\n'.join(messages))
            self.message_box.configure(state='disabled')
        else:
            self.message_box.configure(state='normal')
            self.message_box.delete('1.0', 'end')
            self.message_box.insert('end', "No received messages.\n")
            self.message_box.configure(state='disabled')

    # def handle_received_message(self, message):
    #     print(message)
    #     self.message_label.delete(0, END)
    #     self.message_label.insert(0,message)
    # def handle_received_message(self, message):
    #     self.update_message_label(message)
    #
    # def update_message_label(self, message):
    #     self.message_label.config(state='normal')
    #     self.message_label.delete(0, END)
    #     self.message_label.insert(0, message)
    #     self.message_label.config(state='readonly')

    def close(self):
        self.parent.deiconify()
        self.destroy()