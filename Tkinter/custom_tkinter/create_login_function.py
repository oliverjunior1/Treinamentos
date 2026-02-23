def login():
    username = 'Geeks'
    password = '123456'
    new_window = ctk.CTkTopLevel(app)

    new_window.title('New Window')
    new_window.geometry('350x150')

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title = "Login Successful",
        message = "You have logged in Successfully")
        ctk.CTkLabel(new_window,
                     text="Geeks is best \"
                          "for learning ANYTHING !!").pack()

