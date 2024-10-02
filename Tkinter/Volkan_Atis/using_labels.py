from tkinter import *

root = Tk()
label = Label(root, text='Hello Python')
# label['text'] = "Hello Tkinter"
label.config(text="Hello Tkinter")
label.config(font="Times 15", fg='red')
label.config(bg='yellow')
label.config(text='Hello Python I love you so much')
label.config(wraplength='150')
label.pack()
root.geometry("300x250")
root.mainloop()