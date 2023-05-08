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
class delete_lesson(tkinter.Toplevel):
    def __init__(self, parent, email, password):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title('DELETE LESSON WINDOW')
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
                                      *["kids tennis", "swimming", "yoga", "basketball", "dance", "adults tennis",
                                        "ping pong", "fitness", "pilates", "boxing"])
        self.nameofgroup.config(font=("Helvetica", 14), width=20)
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
                                    *["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"])
        self.lessonday.config(font=("Helvetica", 14), width=20)
        self.lessonday.pack()

        self.buttonPlus = Button(self, text="DELETE LESSON",font=("Helvetica", 14, "bold"), command=self.deletelesson, background="white", activebackground="white",bg="#AFD3E2")
        # self.buttonPlus.place(x=250, y=400, width=120, height=50)
        self.buttonPlus.pack(pady=20)

        # self.str = StringVar()
        # self.str.set("")
        # self.labellogin = Label(self, textvariable=self.str, foreground="red")
        # self.labellogin.place(x=200, y=450)




    def deletelesson(self):
        try:
            if len(self.nameofgroup_var.get()) == 0 or len(self.startH.get()) == 0 or len(self.endH.get()) == 0 or len(
                        self.lessonday_var.get()) == 0:
                messagebox.showerror("please write details", "Error")
                return
            print("DELETE LESSON")
            arr = ["deletelesson", self.nameofgroup_var.get(), self.startH.get(), self.endH.get(),
                       self.lessonday_var.get(), self.email,self.password]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
            data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data)
            if data == "not found":
                messagebox.showerror("notification", "lesson doesnt exist")
            elif data == "Success":
                messagebox.showinfo("notification", "lesson deleted successfully")
                # arr1 = ["Deletegroup", self.nameofgroup_var.get(), self.startH.get(), self.endH.get(),
                #         self.lessonday_var.get()]
                # print(arr1)
                # str_delete1 = ",".join(arr1)
                # print(str_delete1)
                # self.parent.parent.parent.send_msg(str_delete1, self.parent.parent.parent.client_socket)
            elif data == "Failed to delete record":
                messagebox.showerror("notification", "Error, please try again")
            elif data == "not allowed":
                messagebox.showerror("notification", "You are not the teacher of the lesson! You are not allowed to delete it!")
            return True
        except:
            return False


    def close(self):
        self.parent.deiconify()
        self.destroy()