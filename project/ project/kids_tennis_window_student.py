import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkmacosx import Button
from ttkthemes import ThemedTk


class kids_tennis_lesson_student(tkinter.Toplevel):
    def __init__(self, parent, firstname, lastname):
        super().__init__(parent)
        self.parent = parent
        self.title('KIDS TENNIS LESSON WINDOW')
        self.firstname = firstname
        self.lastname = lastname
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
                    row_values = (element[0], element[1], element[2], element[3])
                    item_id = self.tree.insert("", "end", values=row_values, tags=("button",))
                    current_row = self.tree.item(item_id)['values']
                    # print(current_row)
                    # str_current_row = ",".join(current_row)
                    # print(str_current_row)
                    # current_row1 = ["check_grouptime_to_student", "kids tennis", element[0], element[1], element[2], element[3], self.firstname, self.lastname]
                    # print(current_row1)
                    # str_current_row = ",".join(current_row1)
                    # print(str_current_row)
                    # self.parent.parent.parent.send_msg(str_current_row, self.parent.parent.parent.client_socket)
                    # get_str_current_row = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
                    # print(get_str_current_row)
                    # if get_str_current_row == "Exist":
                    #     self.tree.item(item_id, tags=("booked",))
                    #     self.tree.tag_configure("booked", background="green")
                    # elif get_str_current_row == "Not Exist":
                    #     self.tree.item(item_id, tags=("button",))
                    #     self.tree.tag_configure("button", background="white")
                    # self.tree.bind(item_id, lambda event, item_id=item_id: self.book_lesson(item_id))
                    self.tree.bind('<ButtonRelease-1>', self.book_lesson)


    def book_lesson(self, event):
        curItem = self.tree.focus()
        row = self.tree.item(curItem)['values']
        print(row)
        current_tags = self.tree.item(curItem)["tags"]
        if "booked" not in current_tags:
            response = messagebox.askquestion("Book Lesson", "Do you want to book this lesson?")
            if response == 'yes':
                arr_insert = ["insert_grouptime_to_student", "kids tennis", row[0], row[1], row[2], row[3],
                              self.firstname, self.lastname]
                print(arr_insert)
                str_insert = ",".join(arr_insert)
                print(str_insert)
                self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
                get_str = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
                print(get_str)
                if get_str == "Success":
                    messagebox.showinfo("Success", "You booked a lesson successfully")
                    self.tree.item(curItem, tags=("booked",))
                    self.tree.tag_configure("booked", background="green")
                elif get_str == "Student exists":
                    messagebox.showinfo("Notification", "You are already in the group")
                    self.tree.item(curItem, tags=("booked",))
                    self.tree.tag_configure("booked", background="green")
                elif get_str == "error":
                    messagebox.showerror("Error", "booking a lesson failed")
        else:
            response = messagebox.askquestion("Cancel Lesson", "Do you want to cancel this lesson?")
            if response == 'yes':
                arr_delete = ["delete_grouptime_to_student", "kids tennis", row[0], row[1], row[2], row[3],
                              self.firstname, self.lastname]
                print(arr_delete)
                str_delete = ",".join(arr_delete)
                print(str_delete)
                self.parent.parent.parent.send_msg(str_delete, self.parent.parent.parent.client_socket)
                get_str1 = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
                print(get_str1)
                if get_str1 == "Success":
                    messagebox.showinfo("Success", "You canceled a lesson successfully")
                    self.tree.item(curItem, tags=("button",))
                    self.tree.tag_configure("button", background="white")
                elif get_str1 == "You are not in the group":
                    messagebox.showinfo("Notification", "You are not in the group")
                elif get_str1 == "error":
                    messagebox.showerror("Error", "canceling a lesson failed")

    # def book_lesson(self, event):
    #     curItem = self.tree.focus()
    #     row = self.tree.item(curItem)['values']
    #     print(row)
    #     current_tags = self.tree.item(curItem)["tags"]
    #     if "booked" not in current_tags:
    #         response = messagebox.askquestion("Book Lesson", "Do you want to book this lesson?")
    #         if response == 'yes':
    #             messagebox.showinfo("Success", "You booked a lesson successfully")
    #             self.tree.item(curItem, tags=("booked",))
    #             self.tree.tag_configure("booked", background="green")
    #     else:
    #         response = messagebox.askquestion("Cancel Lesson", "Do you want to cancel this lesson?")
    #         if response == 'yes':
    #             messagebox.showinfo("Success", "You canceled a lesson successfully")
    #             self.tree.item(curItem, tags=("button",))
    #             self.tree.tag_configure("button", background="white")

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
