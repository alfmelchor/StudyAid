import customtkinter as ctk
import tkinter as tk


class CredentialsMenu:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.frame = ctk.CTkFrame(self.parent, width=500, height=500, fg_color='#EBEBEB')
        self.frame.grid(row=3, column=3)

        # Header
        # self.appTitle = ctk.CTkLabel(self.parent, width=100, text="Homework Tracker", font=('Arial', 40, 'bold')).grid(row=1, column=3)

        # Body
        self.label = ctk.CTkLabel(self.frame, width=150, text="Welcome", font=('Arial', 20))
        self.label.pack()
        self.userEntry = ctk.CTkEntry(self.frame, width=200, height=30, placeholder_text="Username")
        self.userEntry.pack(pady=10)
        self.passEntry = ctk.CTkEntry(self.frame, width=200, height=30, placeholder_text="Password", show='*')
        self.passEntry.pack(pady=5)
        self.loginButton = ctk.CTkButton(self.frame, width=200, height=30, text="Login", fg_color='#1C9670',
                                         hover_color='#197b5c', command=self.checkCredentials)
        self.loginButton.pack(pady=10)

        self.credentialsMessage = ctk.CTkLabel(self.frame, width=120, height=10, text="")

    def checkCredentials(self):
        if self.userEntry.get() == 'user' and self.passEntry.get() == 'pass':
            self.credentialsMessage.configure(text="")
            self.loginButton.configure(text="Logging in..")
            result = True
        else:
            self.credentialsMessage.configure(text="Incorrect credentials.", text_color="red")
            self.credentialsMessage.pack()
            result = False

        self.callback(result)

    def resetCredentials(self):
        self.credentialsMessage.configure(text="")
        self.userEntry.configure(placeholder_text="Username")
        self.passEntry.configure(placeholder_text="Password")
