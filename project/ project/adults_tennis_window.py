import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button

class adults_tennis_lesson(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('ADULTS TENNIS LESSON WINDOW')
        self.create_table()

        # self.handle_thread_socket1()
        # self.after(500, self.update_table)
        Button(self, text='Close', command=self.close).pack(side=tkinter.BOTTOM, fill=tkinter.X)

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
        self.parent.parent.parent.send_msg("adults tennis", self.parent.parent.parent.client_socket)
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
                    element[0], element[1], element[2], ''))  # add an empty fourth element to each row

    # def handle_thread_socket(self):
    #     client_handler = threading.Thread(target=self.show_info, args=())
    #     client_handler.daemon = True
    #     client_handler.start()



    # def handle_thread_socket1(self):
    #     client_handler = threading.Thread(target=self.update_table, args=())
    #     client_handler.daemon = True
    #     client_handler.start()
    #
    # def add_group(self, arr):
    #     if arr != None and arr[0] == "Addgroup" and arr[1] == "kids tennis" and len(arr) == 5:
    #         self.tree.insert("", END, values=(arr[2], arr[3], arr[4]))
    #
    # def delete_group(self, arr):
    #     if arr != None and arr[0] == "Deletegroup" and arr[1] == "kids tennis" and len(arr) == 5:
    #         for item in self.tree.get_children():
    #             if self.tree.item(item)["values"] == (arr[2], arr[3], arr[4]):
    #                 self.tree.delete(item)
    #                 break
    #
    # def update_group(self, arr):
    #     if arr != None and arr[0] == "Updategroup" and arr[1] == "kids tennis" and len(arr) == 8:
    #         for item in self.tree.get_children():
    #             if self.tree.item(item)["values"] == (arr[5], arr[6], arr[7]):
    #                 self.tree.item(item, values=(arr[2], arr[3], arr[4]))
    #                 break
    #
    # def update_table(self):
    #     data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
    #     if data is not None and data != '':
    #         arr = data.split(",")
    #         if arr != None and arr[0] == "Addgroup" and arr[1] == "kids tennis" and len(arr) == 5:
    #             self.add_group(arr)
    #         elif arr != None and arr[0] == "Deletegroup" and arr[1] == "kids tennis" and len(arr) == 5:
    #             self.delete_group(arr)
    #         elif arr != None and arr[0] == "Updategroup" and arr[1] == "kids tennis" and len(arr) == 8:
    #             self.update_group(arr)
    #     self.after(500, self.update_table)

    # def update_table(self):
    #     data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
    #     if data is not None and data != '':
    #         arr = data.split(",")
    #         if arr != None and arr[0] == "Addgroup" and arr[1] == "kids tennis" and len(arr) == 5:
    #             self.tree.insert("", END, values=(arr[2], arr[3], arr[4]))
    #         elif arr != None and arr[0] == "Deletegroup" and arr[1] == "kids tennis" and len(arr) == 5:
    #             for item in self.tree.get_children():
    #                 if self.tree.item(item)["values"] == (arr[2], arr[3], arr[4]):
    #                     self.tree.delete(item)
    #                     break
    #         elif arr != None and arr[0] == "Updategroup" and arr[1] == "kids tennis" and len(arr) == 8:
    #             for item in self.tree.get_children():
    #                 if self.tree.item(item)["values"] == (arr[5], arr[6], arr[7]):
    #                     self.tree.item(item, values=(arr[2], arr[3], arr[4]))
    #                     break
    #     self.after(500, self.update_table)

    def close(self):
        self.parent.deiconify()
        self.destroy()
