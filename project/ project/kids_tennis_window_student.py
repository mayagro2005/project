import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button

class kids_tennis_lesson_student(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('KIDS TENNIS LESSON WINDOW')
        self.create_table()
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)



    def create_table(self):
        self.tree = ttk.Treeview(self, columns=("START HOUR", "END HOUR", "LESSON DAY", "NAME OF TEACHER", "BOOK/CANCEL", "PARTICIPANTS"),
                                 show="headings")
        self.tree.column("START HOUR", width=150, anchor='center')
        self.tree.column("END HOUR", width=150, anchor='center')
        self.tree.column("LESSON DAY", width=150, anchor='center')
        self.tree.column("NAME OF TEACHER", width=150, anchor='center')
        self.tree.column("BOOK/CANCEL", width=150, anchor='center')
        self.tree.column("PARTICIPANTS", width=150, anchor='center')
        self.tree.heading("START HOUR", text="START HOUR")
        self.tree.heading("END HOUR", text="END HOUR")
        self.tree.heading("LESSON DAY", text="LESSON DAY")
        self.tree.heading("NAME OF TEACHER", text="NAME OF TEACHER")
        self.tree.heading("BOOK/CANCEL", text="BOOK/CANCEL")
        self.tree.heading("PARTICIPANTS", text="PARTICIPANTS")
        self.tree.pack(fill=BOTH, expand=True)
        self.show_info()

    def show_info(self):
        print(self.parent.parent.parent.client_socket)
        self.parent.parent.parent.send_msg("kids tennis", self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        if data is not None and data != '':
            if data == "there is no group" or data == "error":
                pass
            else:
                arr = data.split("*")
                print(arr)
                for el in arr:
                    element = el.split(",")
                    button = Button(self.tree, text="BOOK", bg="green", command=self.book_lesson)
                    self.tree.insert("", END, values=(element[0], element[1], element[2], element[3], button, ''))

    def book_lesson(self):
        item = self.tree.focus()
        if item:
            current_text = self.tree.item(item)["values"][4]
            if current_text == "BOOK":
                messagebox.showinfo("Success", "You booked a lesson successfully")
                self.tree.item(item, tags=("booked",))
                self.tree.tag_configure("booked", background="green")
                self.tree.set(item, "BOOK/CANCEL", "CANCEL")

            elif current_text == "CANCEL":
                messagebox.showinfo("Success", "You canceled a lesson successfully")
                self.tree.item(item, tags=("cancelled",))
                self.tree.tag_configure("cancelled", background="red")
                self.tree.set(item, "BOOK/CANCEL", "BOOK")


    def close(self):
        self.parent.deiconify()
        self.destroy()
