from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title('Text widget Example')

text = Text(root, height=8)
text.pack()

root.mainloop()
