import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('240x100')
root.title('Login')
root.resizable(0,0)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

username_label = ttk.Label(root, text='Username:')
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

user_entry = ttk.Entry(root)
user_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

password_label = ttk.Label(root, text='Password')
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root, show='*')
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

login_button = ttk.Button(root, text='Login')
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()



