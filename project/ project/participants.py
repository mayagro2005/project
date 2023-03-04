import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button
from ttkthemes import ThemedTk


class Participants(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('PARTICIPANTS')
        self.create_table()
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)

    def create_table(self):
        self.tree = ttk.Treeview(self, columns=(
        "START HOUR", "END HOUR", "LESSON DAY", "NAME OF TEACHER"),
                                 show="headings")
        self.tree.column("START HOUR", width=150, anchor='center')
        self.tree.column("END HOUR", width=150, anchor='center')
        self.tree.column("LESSON DAY", width=150, anchor='center')
        self.tree.column("NAME OF TEACHER", width=150, anchor='center')
        self.tree.heading("START HOUR", text="START HOUR")
        self.tree.heading("END HOUR", text="END HOUR")
        self.tree.heading("LESSON DAY", text="LESSON DAY")
        self.tree.heading("NAME OF TEACHER", text="NAME OF TEACHER")
        self.tree.pack(fill=BOTH, expand=True)

    def close(self):
        self.parent.deiconify()
        self.destroy()
