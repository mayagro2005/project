import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button

class kids_tennis_lesson(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('KIDS TENNIS LESSON WINDOW')
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
        self.tree = ttk.Treeview(self, columns=("START HOUR", "END HOUR", "LESSON DAY", "NAMES OF PARTICIPANTS"),
                                 show="headings")
        self.tree.column("START HOUR", width=150, anchor='center')
        self.tree.column("END HOUR", width=150, anchor='center')
        self.tree.column("LESSON DAY", width=150, anchor='center')
        self.tree.column("NAMES OF PARTICIPANTS", width=150, anchor='center')
        self.tree.heading("START HOUR", text="START HOUR")
        self.tree.heading("END HOUR", text="END HOUR")
        self.tree.heading("LESSON DAY", text="LESSON DAY")
        self.tree.heading("NAMES OF PARTICIPANTS", text="NAMES OF PARTICIPANTS")
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
                    self.tree.insert("", END, values=(
                    element[0], element[1], element[2], ''))  # add an empty fourth ele

    def close(self):
        self.parent.deiconify()
        self.destroy()
