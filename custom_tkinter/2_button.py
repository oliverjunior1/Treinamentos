import customtkinter

def button_callback():
    print("Button clicked")

app = customtkinter.CTk()
app.title("my app")
app.geometry('400x150')

button = customtkinter.CTkButton(app, text="my Button", command=button_callback)
button.grid(row=0, column=0, pady=20, padx=20)

app.mainloop()