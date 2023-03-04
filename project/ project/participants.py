import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button
from ttkthemes import ThemedTk


class Participants(tkinter.Toplevel):
    def __init__(self, parent, nameofgroup, startH, endH, lessonDay, teachername):
        super().__init__(parent)
        self.parent = parent
        self.title('PARTICIPANTS')
        self.nameofgroup = nameofgroup
        self.startH = startH
        self.endH = endH
        self.lessonDay = lessonDay
        self.teachername = teachername
        self.create_table()
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)


    def create_table(self):
        self.tree = ttk.Treeview(self, columns=(
        "PARTICIPANTS"),show="headings")
        self.tree.column("PARTICIPANTS", width=150, anchor='center')
        self.tree.heading("PARTICIPANTS", text="PARTICIPANTS")
        self.tree.pack(fill=BOTH, expand=True)
        self.show_info()

    def show_info(self):
        arr_get_students = ["get_students_of_group", self.nameofgroup, self.startH, self.endH, self.lessonDay,
                            self.teachername]
        str_get_students = ",".join(arr_get_students)
        self.parent.parent.parent.parent.send_msg(str_get_students, self.parent.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.parent.recv_msg(self.parent.parent.parent.parent.client_socket)
        if data is None or data == '':
            pass
        else:
            arr = data.split("*")
            count = len(arr)
            self.tree.insert("", END, values=(f"{count} participants",), tags=('bold', 'red'))
            self.tree.tag_configure('bold', font=('TkDefaultFont', 10, 'bold'))
            self.tree.tag_configure('red', foreground='red')
            for el in arr:
                element = el.split(",")
                name = " ".join(element[:])
                self.tree.insert("", END, values=(name,))

    def close(self):
        self.parent.deiconify()
        self.destroy()
