from tkinter import *

root = Tk()

def callback():
    label.config(text='You clicked me', fg='red', bg='yellow')

label = Label(root, text='Hello Python')
label.pack()
button = Button(root, text='Click me', command=callback)
button.pack()
# button['state'] = 'disabled'
button['state'] = 'normal'

root.geometry('350x300')
root.mainloop()