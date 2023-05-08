import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button
from participants import Participants
class swimming_lesson(tkinter.Toplevel):
    def __init__(self, parent,firstname,lastname):
        super().__init__(parent)
        self.parent = parent
        self.title('SWIMMING LESSON WINDOW')
        self.firstname = firstname
        self.lastname = lastname
        self.create_table()
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)

    # def create_table(self):
    #     self.tree = ttk.Treeview(self, columns=("START HOUR", "END HOUR", "LESSON DAY", "NAMES OF PARTICIPANTS", "NAME OF TEACHER"), show="headings")
    #     self.tree.column("START HOUR", width=150, anchor='center')
    #     self.tree.column("END HOUR", width=150, anchor='center')
    #     self.tree.column("LESSON DAY", width=150, anchor='center')
    #     self.tree.column("NAMES OF PARTICIPANTS", width=150, anchor='center')
    #     self.tree.column("NAME OF TEACHER", width=150, anchor='center')
    #     self.tree.heading("START HOUR", text="START HOUR")
    #     self.tree.heading("END HOUR", text="END HOUR")
    #     self.tree.heading("LESSON DAY", text="LESSON DAY")
    #     self.tree.heading("NAMES OF PARTICIPANTS", text="NAMES OF PARTICIPANTS")
    #     self.tree.heading("NAME OF TEACHER", text="NAME OF TEACHER")
    #     self.tree.pack(fill=BOTH, expand=True)
    #     self.show_info()
    #
    # def show_info(self):
    #     self.parent.parent.parent.send_msg("kids tennis", self.parent.parent.parent.client_socket)
    #     data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
    #     dataforteacher = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
    #     if data is not None and data != '':
    #         if data == "there is no group" or data == "error":
    #             pass
    #         else:
    #             arr_data = data.split("*")
    #             arr_teacher = []
    #             if dataforteacher and dataforteacher.startswith("teachername kids tennis"):
    #                 arr_teacher = dataforteacher.split("*")[2:]
    #             for i, group in enumerate(arr_data):
    #                 element = group.split(",")
    #                 teacher = arr_teacher[i] if i < len(arr_teacher) else ""
    #                 self.tree.insert("", END, values=(element[0], element[1], element[2], '', teacher))





    def create_table(self):
        self.tree = ttk.Treeview(self, columns=("START HOUR", "END HOUR", "LESSON DAY", "NAME OF TEACHER"),
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
        self.show_info()

    def show_info(self):
        print(self.parent.parent.parent.client_socket)
        self.parent.parent.parent.send_msg("swimming", self.parent.parent.parent.client_socket)
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
                    row_values = (element[0], element[1], element[2], element[3])
                    item_id = self.tree.insert("", "end", values=row_values, tags=("button",))
                    # self.tree.bind(item_id, lambda event, item_id=item_id: self.book_lesson(item_id))
                    teacher_firstname, teacher_lastname = element[3].split()
                    if teacher_firstname == self.firstname and teacher_lastname == self.lastname:
                        self.tree.item(item_id, tags=("booked",))
                        self.tree.tag_configure("booked", background="red")
                    else:
                        self.tree.item(item_id, tags=("button",))
                        self.tree.tag_configure("button", background="white")
                    self.tree.bind('<ButtonRelease-1>', self.book_lesson)

    def book_lesson(self, event):
        curItem = self.tree.focus()
        row = self.tree.item(curItem)['values']
        print(row)
        current_tags = self.tree.item(curItem)["tags"]
        response = messagebox.askquestion("PARTICIPANTS", "Do you want to see the paticipants?")
        if response == 'yes':
            window = Participants(self,"swimming",row[0],row[1],row[2],row[3])
            window.grab_set()


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
