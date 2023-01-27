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
class update_lesson(tkinter.Toplevel):
    def __init__(self, parent, email, password):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('UPDATE LESSON WINDOW')
        self.email = email
        self.password = password

        self.create_gui()
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # Button(self, text='Close', command=self.close).pack(side=BOTTOM)
        # Button.place(x=220,y=580)

    def create_gui(self):
        self.lbl_update1 = Label(self, text="write the details lesson you "
                                           "\n want to update below: ", background="light blue",
                                 foreground="black", font=("Calibri", 14))
        self.lbl_update1.place(x=10, y=70)
        self.lbl_nameofgroup = Label(self, width=10, text="name of group ")
        self.lbl_nameofgroup.place(x=220, y=20)
        self.nameofgroup = Entry(self, width=10)
        self.nameofgroup.place(x=330, y=20)
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
        self.lbl_startH1 = Label(self, width=10, text="start hour")
        self.lbl_startH1.place(x=10, y=130)
        self.startH1 = Entry(self, width=10)
        self.startH1.place(x=120, y=130)

        self.lbl_endH1 = Label(self, width=10, text="end hour")
        self.lbl_endH1.place(x=10, y=180)
        self.endH1 = Entry(self, width=10)
        self.endH1.place(x=120, y=180)

        self.lbl_lessonday1 = Label(self, width=10, text="lesson day")
        self.lbl_lessonday1.place(x=10, y=230)
        self.lessonday1 = Entry(self, width=10)
        self.lessonday1.place(x=120, y=230)

        # self.lbl_password = Label(self, width=10, text="password :")
        # self.lbl_password.place(x=10, y=250)
        # self.password = Entry(self, width=20)
        # self.password.place(x=150, y=250)

        self.buttonPlus = Button(self, text="UPDATE LESSON", command=self.updatelesson, background="white")
        self.buttonPlus.place(x=250, y=400,width=120, height=50)

        # self.str = StringVar()
        # self.str.set("")
        # self.labellogin = Label(self, textvariable=self.str, foreground="red")
        # self.labellogin.place(x=200, y=450)
        self.lbl_update = Label(self, text="write the updated "
                                           "\n details below: ", background="light blue",
                                foreground="black", font=("Calibri", 14))
        self.lbl_update.place(x=280, y=70)
        # self.lbl_nameofgroup = Label(self, width=10, text="name of group ")
        # self.lbl_nameofgroup.place(x=280, y=80)
        # self.nameofgroup = Entry(self, width=10)
        # self.nameofgroup.place(x=390, y=80)

        # phase 1 button
        self.lbl_startH = Label(self, width=10, text="start hour")
        self.lbl_startH.place(x=280, y=130)
        self.startH = Entry(self, width=10)
        self.startH.place(x=390, y=130)

        self.lbl_endH = Label(self, width=10, text="end hour")
        self.lbl_endH.place(x=280, y=180)
        self.endH = Entry(self, width=10)
        self.endH.place(x=390, y=180)

        self.lbl_lessonday = Label(self, width=10, text="lesson day")
        self.lbl_lessonday.place(x=280, y=230)
        self.lessonday = Entry(self, width=10)
        self.lessonday.place(x=390, y=230)


    def updatelesson(self):
        try:
            if len(self.nameofgroup.get()) == 0 or len(self.startH.get()) == 0 or len(self.endH.get()) == 0 or len(
                        self.lessonday.get()) == 0 or len(self.startH1.get()) == 0 or len(self.endH1.get()) == 0 or len(
                        self.lessonday1.get()) == 0:
                messagebox.showerror("please complete the details", "Error")
                return
            print("UPDATE LESSON")
            arr = ["updatelesson", self.nameofgroup.get(), self.startH.get(), self.endH.get(),
                       self.lessonday.get(), self.startH1.get(), self.endH1.get(),
                       self.lessonday1.get(), self.email,self.password]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
            data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data)
            if data == "not exist":
                messagebox.showerror("notification", "the lesson you want to update doesnt exist")
            elif data == "Success":
                messagebox.showinfo("notification", "lesson updated successfully")
            elif data == "Failed":
                messagebox.showerror("notification", "Error, please try again")
            arr1 = [self.nameofgroup.get(), self.startH.get(), self.endH.get(),
                       self.lessonday.get(), self.email,self.password]
            print(arr1)
            return True
        except:
            return False


    def close(self):
        self.parent.deiconify()
        self.destroy()