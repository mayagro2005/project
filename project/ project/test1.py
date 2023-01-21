import tkinter as tk
from tkinter import messagebox

def open_message_window(self):
    message_window = tk.Toplevel(self)
    message_window.title("Write a message")

    # Create a Text widget for the user to write messages
    message_text = tk.Text(message_window)
    message_text.pack()

    # Create a button to submit the message
    submit_button = tk.Button(message_window, text="Submit", command=lambda: submit_message(message_text))
    submit_button.pack()

def submit_message(message_text):
    message = message_text.get("1.0", "end-1c")
    # Do something with the message (e.g. save to a file or database)
    messagebox.showinfo("Success", "Message submitted: " + message)


# root = Tk()
# app = MyWindow(master=root)
# app.mainloop()

