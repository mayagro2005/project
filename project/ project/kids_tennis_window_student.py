import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button
from ttkthemes import ThemedTk


class kids_tennis_lesson_student(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('KIDS TENNIS LESSON WINDOW')
        self.create_table()
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)

    def create_table(self):
        self.tree = ttk.Treeview(self, columns=(
        "START HOUR", "END HOUR", "LESSON DAY", "NAME OF TEACHER", "PARTICIPANTS"),
                                 show="headings")
        self.tree.column("START HOUR", width=150, anchor='center')
        self.tree.column("END HOUR", width=150, anchor='center')
        self.tree.column("LESSON DAY", width=150, anchor='center')
        self.tree.column("NAME OF TEACHER", width=150, anchor='center')
        self.tree.column("PARTICIPANTS", width=150, anchor='center')
        self.tree.heading("START HOUR", text="START HOUR")
        self.tree.heading("END HOUR", text="END HOUR")
        self.tree.heading("LESSON DAY", text="LESSON DAY")
        self.tree.heading("NAME OF TEACHER", text="NAME OF TEACHER")
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
                    row_values = (element[0], element[1], element[2], element[3], '')
                    item_id = self.tree.insert("", "end", values=row_values, tags=("button",))
                    # self.tree.bind(item_id, lambda event, item_id=item_id: self.book_lesson(item_id))
                    self.tree.bind('<ButtonRelease-1>', self.book_lesson)

    def book_lesson(self, event):
        curItem = self.tree.focus()
        # row = self.tree.item(curItem)['values']
        current_text = self.tree.item(curItem)["values"][4]
        if current_text == "":
            response = messagebox.askquestion("Book Lesson", "Do you want to book this lesson?")
            if response == 'yes':
                messagebox.showinfo("Success", "You booked a lesson successfully")
                self.tree.item(curItem, tags=("booked",))
                self.tree.tag_configure("booked", background="green")
                self.tree.set(curItem, "PARTICIPANTS", "1/4")
        elif current_text == "1/4":
            response = messagebox.askquestion("Cancel Lesson", "Do you want to cancel this lesson?")
            if response == 'yes':
                messagebox.showinfo("Success", "You canceled a lesson successfully")
                self.tree.item(curItem, tags=("button",))
                self.tree.tag_configure("button", background="white")
                self.tree.set(curItem, "PARTICIPANTS", "")

    def selectItem(self, a):
        curItem = self.tree.focus()
        row =self.tree.item(curItem)['values']
        print(row)
        #print(curItem)
        #rint(self.tree.item(curItem))
        #curRow = self.tree.set(a)
        #loc_value = curRow["START HOUR"]
        #print(loc_value)

    def close(self):
        self.parent.deiconify()
        self.destroy()
