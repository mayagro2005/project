import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button

class tennis_lesson(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('INSERT LESSON WINDOW')
        self.ListData = [
            ("START HOUR", "END HOUR", "LESSON DAY"),
        ]
        self.create_table()

    def create_table(self):
        totalrow = len(self.ListData)
        totalcolum = len(self.ListData[0])
        for i in range(totalrow):
            for j in range(totalcolum):
                self.e = Entry(width=22, fg='blue',font=('Arial', 15, 'bold'))
                self.e.grid(row=i,column=j)
                self.e.insert(END,self.ListData[i][j])

    def update_table(self):
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        arr = data.split(",")
        if arr != None and arr[0] == "Addgroup" and arr[1] == "kids tennis" and len(arr) == 5:
            self.update_table(data)
            self.ListData.append((arr[2], arr[3], arr[4]))
            self.create_table()








