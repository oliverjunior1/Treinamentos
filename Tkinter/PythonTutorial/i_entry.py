import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x150')
root.resizable(False, False)
root.title('Sign In')

email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    msg= f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(
        title = 'Information',
        message=msg
    )

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

email_label = ttk.Label(signin, text='Email Address')
email_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show='*')
password_entry.pack(fill='x', expand=True)

login_button = ttk.Button(signin, text='Login', command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()