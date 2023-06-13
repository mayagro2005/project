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
        self.title('INSERT LESSON WINDOW')
        self.email = email
        self.password = password
        self.config(bg="#AFD3E2")

        self.create_gui()
        Button(self, text='Close',font=("Helvetica", 12, "bold"), command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)
        # Button(self, text='Close', command=self.close).pack(expand=True, side=BOTTOM)

    def create_gui(self):
        self.nameofgroup_var = StringVar()
        self.lbl_nameofgroup = Label(self, text="Name of Group", font=("Helvetica", 16, "bold"),bg="#AFD3E2")
        self.lbl_nameofgroup.pack(pady=20)
        self.nameofgroup = OptionMenu(self, self.nameofgroup_var,
                                    *["kids tennis", "swimming", "yoga", "basketball", "dance","adults tennis","ping pong","fitness","pilates","boxing"])
        self.nameofgroup.config(font=("Helvetica", 14), width=20,bg="#AFD3E2")
        self.nameofgroup.pack()

        # Start Hour
        self.lbl_startH = Label(self, text="Start Hour", font=("Helvetica", 16, "bold"),bg="#AFD3E2")
        self.lbl_startH.pack(pady=20)
        self.startH = Entry(self, font=("Helvetica", 14), width=20)
        self.startH.pack()

        # End Hour
        self.lbl_endH = Label(self, text="End Hour", font=("Helvetica", 16, "bold"),bg="#AFD3E2")
        self.lbl_endH.pack(pady=20)
        self.endH = Entry(self, font=("Helvetica", 14), width=20)
        self.endH.pack()

        self.lessonday_var = StringVar()
        # Lesson Day
        self.lbl_lessonday = Label(self, text="Lesson Day", font=("Helvetica", 16, "bold"),bg="#AFD3E2")
        self.lbl_lessonday.pack(pady=20)
        self.lessonday = OptionMenu(self, self.lessonday_var,
                                    *["Sunday","Monday", "Tuesday", "Wednesday", "Thursday"])
        self.lessonday.config(font=("Helvetica", 14), width=20,bg="#AFD3E2")
        self.lessonday.pack()

        # INSERT LESSON button
        self.buttonPlus = Button(self, text="INSERT LESSON", font=("Helvetica", 14, "bold"), command=self.insertlesson,
                                 background="white", activebackground="white")
        self.buttonPlus.pack(pady=20)


    def insertlesson(self):
        try:
            if len(self.nameofgroup_var.get()) == 0 or len(self.startH.get()) == 0 or len(self.endH.get()) == 0 or len(
                        self.lessonday_var.get()) == 0:
                messagebox.showerror("please write details", "Error")
                return
            print("INSERT LESSON")
            arr = ["Insertlesson", self.nameofgroup_var.get(), self.startH.get(), self.endH.get(),
                       self.lessonday_var.get(), self.email,self.password]
            print(arr)
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket,"encrypted")
            data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data)
            if data == "collision":
                messagebox.showinfo("notification", "There is a collision with existing lessons")
            elif data == "inserted":
                messagebox.showinfo("notification", "lesson inserted successfully")
                # arr1 = ["Addgroup",self.nameofgroup_var.get(), self.startH.get(), self.endH.get(),
                #         self.lessonday_var.get()]
                # print(arr1)
                # str_insert1 = ",".join(arr1)
                # print(str_insert1)
                # self.parent.parent.parent.send_msg(str_insert1, self.parent.parent.parent.client_socket)
            elif data == "not inserted":
                messagebox.showerror("notification", "Error, please try again")
            return True
        except:
            return False


    def close(self):
        self.parent.deiconify()
        self.destroy()