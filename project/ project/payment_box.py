import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from dbteachers import teachers
from dbstudents import students
import socket
from rgb import rgbprint
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class Payments(tkinter.Toplevel):
    def __init__(self, parent, email, password):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x500')
        self.title('PAYMENT BOX')
        self.email = email
        self.password = password

        self.create_gui()
        # Button(self, text='Close', command=self.close).pack(expand=True, side = BOTTOM)
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # self.close_button = Button(self, text='Close', command=self.close)
        # self.close_button.grid(row=100, column=0, sticky='s')

    def create_gui(self):
        self.lbl_welcome = Label(self, text="Hello! this is your payment box ",background="light blue", foreground="black", font=("Calibri",14))
        self.lbl_welcome.place(x=160, y=20)
        self.lbl_price = Label(self, text="The price for a year is 1500 shekels ",background="light blue", foreground="black", font=("Calibri",14))
        self.lbl_price.place(x=150,y=60)
        self.lbl_paymentmessage = Label(self, text="please pay here: ")
        self.lbl_paymentmessage.place(x=50, y=400)
        self.writepayment = Entry(self, width=20)
        self.writepayment.place(x=250, y=400)
        self.send_message_button = Button(self, text='Pay', command= self.payment)
        self.send_message_button.place(x=190, y=430)
        self.message_label = Entry(self, width=30,foreground="red")
        self.message_label.place(x=120, y=120)
        # self.message_label.grid(row=0, column=0, columnspan=2)
        self.message_label.insert(0, "received messages")
        self.message_label.config(state='readonly')
        self.send_message_button = Button(self, text='CHECK MY PAYMENT', command= self.check_payment)
        self.send_message_button.place(x=120, y=200)

    def check_payment(self):
        arr_payment = ["check_payment", self.email, self.password]
        print(arr_payment)
        str_payment = ",".join(arr_payment)
        print(str_payment)
        self.parent.parent.parent.send_msg(str_payment, self.parent.parent.parent.client_socket)
        get_payment = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(get_payment)
        pay_the_rest = 1500 - int(get_payment)
        if pay_the_rest == 0:
            messagebox.showinfo("Notification", "YOU PAYED EVERYTHING")
        else:
            messagebox.showinfo("Notification", "YOU PAYED" + " " + str(get_payment) + " " + "SHEKELS" + '\n' +
                                "YOU HAVE TO PAY" + " " + str(pay_the_rest) + " " + "SHEKELS")

    def payment(self):
        arr_payment = ["payment", self.writepayment.get(), self.email, self.password]
        print(arr_payment)
        str_payment = ",".join(arr_payment)
        print(str_payment)
        self.parent.parent.parent.send_msg(str_payment, self.parent.parent.parent.client_socket)
        get_payment = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(get_payment)
        if get_payment == "Please pay the exact sum of money":
            messagebox.showinfo("Notification", "PLEASE PAY THE EXACT SUM OF MONEY")
        elif get_payment == "You paid everything":
            messagebox.showinfo("Notification", "YOU PAYED EVERYTHING")
        elif get_payment == "already payed":
            messagebox.showinfo("Notification", "YOU ALREADY PAYED EVERYTHING")
        elif get_payment == "Error":
            messagebox.showinfo("Notification", "PAYMENT FAILED, PLEASE TRY AGAIN")
        else:
            messagebox.showinfo("Notification", "PLEASE PAY" + " " + get_payment + " " + "TO GET TO 1500 SHEKELS")


    def close(self):
        self.parent.deiconify()
        self.destroy()