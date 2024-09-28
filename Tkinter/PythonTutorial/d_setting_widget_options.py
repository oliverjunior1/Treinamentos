# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# ttk.Label(root, text='Hi, there').pack()
#
# root.mainloop()
####################################################################################
import tkinter as tk
from tkinter import ttk

root= tk.Tk()

label = ttk.Label(root)
label['text']= 'Hi, there'
label.pack()

root.mainloop()


