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
        self.config(bg="#AFD3E2")
        self['borderwidth'] = 0

        self.create_gui()
        Button(self, text='Close',font=("Helvetica", 12, "bold"), command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # Button(self, text='Close', command=self.close).pack(side=BOTTOM)
        # Button.place(x=220,y=580)

    def create_gui(self):
        self.lbl_update1 = Label(self, text="write the details lesson you "
                                           "\n want to update below: ", background="#D9ACF5",
                                 foreground="black", font=("Helvetica", 16, "bold"),relief="solid", bd=3)
        self.lbl_update1.place(x=10, y=70)
        self.nameofgroup_var = StringVar()
        self.lbl_nameofgroup1 = Label(self, width=20, text="Name of group", font=("Helvetica", 16, "bold"),bg="#AFD3E2")
        self.lbl_nameofgroup1.place(x=160, y=20)
        self.nameofgroup = OptionMenu(self, self.nameofgroup_var,
                                      *["kids tennis", "swimming", "yoga", "basketball", "dance", "adults tennis",
                                        "ping pong", "fitness", "pilates", "boxing"])
        self.nameofgroup.config(font=("Helvetica", 14), width=10,bg="#AFD3E2")
        self.nameofgroup.pack()
        self.nameofgroup.place(x=330,y=20)


        # phase 1 button
        self.lbl_startH1 = Label(self, width=10, text="start hour",font=("Arial", 13, "bold"),bg="#AFD3E2")
        self.lbl_startH1.place(x=10, y=130)
        self.startH1 = Entry(self, width=10)
        self.startH1.place(x=120, y=130)

        self.lbl_endH1 = Label(self, width=10, text="end hour",font=("Arial", 13, "bold"),bg="#AFD3E2")
        self.lbl_endH1.place(x=10, y=180)
        self.endH1 = Entry(self, width=10)
        self.endH1.place(x=120, y=180)

        self.lessonday_var1 = StringVar()
        self.lbl_lessonday1 = Label(self, width=10, text="lesson day",font=("Arial", 13, "bold"),bg="#AFD3E2")
        self.lbl_lessonday1.place(x=10, y=230)
        self.lessonday1 = OptionMenu(self, self.lessonday_var1,
                                    *["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"])
        self.lessonday1.config(font=("Helvetica", 14), width=10,bg="#AFD3E2")
        self.lessonday1.pack()
        self.lessonday1.place(x=120, y=230)



        self.buttonPlus = Button(self, text="UPDATE LESSON",font=("Helvetica", 14, "bold"), command=self.updatelesson, background="white", activebackground="white",bg="#AFD3E2")
        self.buttonPlus.place(x=200, y=400,width=140, height=50)


        self.lbl_update = Label(self, text="write the updated "
                                           "\n details below: ", background="#D9ACF5",
                                foreground="black", font=("Helvetica", 16, "bold"),relief="solid", bd=3)
        self.lbl_update.place(x=280, y=70)
        self.lbl_startH = Label(self, width=10, text="start hour", font=("Arial", 13, "bold"),bg="#AFD3E2")
        self.lbl_startH.place(x=280, y=130)
        self.startH = Entry(self, width=10)
        self.startH.place(x=390, y=130)

        self.lbl_endH = Label(self, width=10, text="end hour", font=("Arial", 13, "bold"),bg="#AFD3E2")
        self.lbl_endH.place(x=280, y=180)
        self.endH = Entry(self, width=10)
        self.endH.place(x=390, y=180)

        self.lessonday_var = StringVar()
        self.lbl_lessonday = Label(self, width=10, text="lesson day", font=("Arial", 13, "bold"),bg="#AFD3E2")
        self.lbl_lessonday.place(x=280, y=230)
        self.lessonday = OptionMenu(self, self.lessonday_var,
                                     *["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"])
        self.lessonday.config(font=("Helvetica", 14), width=10)
        self.lessonday.pack()
        self.lessonday.place(x=390, y=230)

        # phase 1 button
        # self.lbl_startH = Label(self, width=10, text="start hour")
        # self.lbl_startH.place(x=280, y=130)
        # self.startH = Entry(self, width=10)
        # self.startH.place(x=390, y=130)
        #
        # self.lbl_endH = Label(self, width=10, text="end hour")
        # self.lbl_endH.place(x=280, y=180)
        # self.endH = Entry(self, width=10)
        # self.endH.place(x=390, y=180)
        #
        # self.lbl_lessonday = Label(self, width=10, text="lesson day")
        # self.lbl_lessonday.place(x=280, y=230)
        # self.lessonday = Entry(self, width=10)
        # self.lessonday.place(x=390, y=230)


    def updatelesson(self):
        try:
            if len(self.nameofgroup_var.get()) == 0 or len(self.startH.get()) == 0 or len(self.endH.get()) == 0 or len(
                        self.lessonday_var.get()) == 0 or len(self.startH1.get()) == 0 or len(self.endH1.get()) == 0 or len(
                        self.lessonday_var1.get()) == 0:
                messagebox.showerror("please complete the details", "Error")
                return
            print("UPDATE LESSON")
            arr = ["updatelesson", self.nameofgroup_var.get(), self.startH.get(), self.endH.get(),
                       self.lessonday_var.get(), self.startH1.get(), self.endH1.get(),
                       self.lessonday_var1.get(), self.email,self.password]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
            data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data)
            if data == "not exist":
                messagebox.showerror("notification", "the lesson you want to update doesnt exist")
            elif data == "Success":
                messagebox.showinfo("notification", "lesson updated successfully")
                # arr = ["Updategroup", self.nameofgroup_var.get(), self.startH.get(), self.endH.get(),
                #        self.lessonday_var.get(), self.startH1.get(), self.endH1.get(),
                #        self.lessonday_var1.get()]
                # str_insert = ",".join(arr)
                # print(str_insert)
                # self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
            elif data == "Failed":
                messagebox.showerror("notification", "Error, please try again")
            elif data == "not allowed":
                messagebox.showerror("notification", "You are not the teacher of the lesson! You are not allowed to update it!")

            return True
        except:
            return False


    def close(self):
        self.parent.deiconify()
        self.destroy()