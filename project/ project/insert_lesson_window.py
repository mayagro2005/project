import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button
#https://www.pythontutorial.net/tkinter/tkinter-toplevel/
#toplevel = tk.Toplevel(window) #'toplevel' can be changed to anything,
#it is just a variable to hold the top level, 'window'
#should be whatever variable holds your main window
#toplevel.title = 'Top Level'
class insert_lesson(tkinter.Toplevel):
    def __init__(self, parent, email, password):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('LOGIN WINDOW')
        self.email = email
        self.password = password

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        self.lbl_nameofgroup = Label(self, width=10, text="name of group ")
        self.lbl_nameofgroup.place(x=10, y=50)
        self.nameofgroup = Entry(self, width=20)
        self.nameofgroup.place(x=200, y=50)
        # self.lbl_recognize = Label(self, text="Are you a teacher or student?")
        # self.lbl_recognize.place(x=10, y=50)

        # self.var = StringVar()
        # self.var.set("teacher")
        #
        # self.teacher_radiobutton = Radiobutton(self, text="Teacher", variable=self.var, value="teacher")
        # self.teacher_radiobutton.place(x=200, y=50)
        #
        # self.student_radiobutton = Radiobutton(self, text="Student", variable=self.var, value="student")
        # self.student_radiobutton.place(x=290, y=50)


        # phase 1 button
        self.lbl_startH = Label(self, width=10, text="start hour")
        self.lbl_startH.place(x=10, y=100)
        self.startH = Entry(self, width=20)
        self.startH.place(x=150, y=100)

        self.lbl_endH = Label(self, width=10, text="end hour")
        self.lbl_endH.place(x=10, y=150)
        self.endH = Entry(self, width=20)
        self.endH.place(x=150, y=150)

        self.lbl_lessonday = Label(self, width=10, text="lesson day")
        self.lbl_lessonday.place(x=10, y=200)
        self.lessonday = Entry(self, width=20)
        self.lessonday.place(x=150, y=200)

        # self.lbl_password = Label(self, width=10, text="password :")
        # self.lbl_password.place(x=10, y=250)
        # self.password = Entry(self, width=20)
        # self.password.place(x=150, y=250)

        self.buttonPlus = Button(self, text="INSERT LESSON", command=self.insertlesson, width=100, background="white")
        self.buttonPlus.place(x=50, y=350)

        # self.str = StringVar()
        # self.str.set("")
        # self.labellogin = Label(self, textvariable=self.str, foreground="red")
        # self.labellogin.place(x=200, y=450)




    def insertlesson(self):
        try:
            if len(self.nameofgroup.get()) == 0 or len(self.startH.get()) == 0 or len(self.endH.get()) == 0 or len(
                        self.lessonday.get()) == 0:
                messagebox.showerror("please write details", "Error")
                return
            print("INSERT LESSON")
            arr = ["Insertlesson", self.nameofgroup.get(), self.startH.get(), self.endH.get(),
                       self.lessonday.get(), self.email,self.password]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
            data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data)
            if data == "exist":
                messagebox.showinfo("notification", "lesson already exists")
            elif data == "inserted":
                messagebox.showinfo("notification", "lesson inserted successfully")
            elif data == "not inserted":
                messagebox.showerror("notification", "Error, please try again")
            arr1 = [self.nameofgroup.get(), self.startH.get(), self.endH.get(),
                       self.lessonday.get(), self.email,self.password]
            print(arr1)
        except:
            return False


    def close(self):
        self.parent.deiconify()
        self.destroy()