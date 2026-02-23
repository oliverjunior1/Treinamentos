import customtkinter
def button_callback():
    print("Button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("450x500")
app.grid_columnconfigure((0), weight=1)

button = customtkinter.CTkButton(app, text='my button', command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky='ew', columnspan=2)
checkbox_1 = customtkinter.CTkCheckBox(app, text='checkbox 1')
checkbox_1.grid()
checkbox_2 = customtkinter.CTkCheckBox(app, text='checkbox 2')


app.mainloop()