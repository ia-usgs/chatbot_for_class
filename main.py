import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
import sqlite3

import mainframe

from dashboard_screen import DashboardScreen
from register_screen import RegisterScreen
from Forgot_Password import ForgotPasswordScreen


class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Financial Chatbot")
        self.geometry("800x600")
        self.configure(bg="black")
        self.create_widgets()
    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="20 20 20 20", style= 'MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #Title
        title_label = ttk.Label(mainframe, text="Login to your account", font=("Helvetica", 20, "bold"), style='Title.TLabel')
        title_label.grid(column=1, row=0, columnspan=2, pady=20)

        #Login Labels
        username_label = ttk.Label(mainframe, text="Username", font=("Helvetica", 12), style='Label.TLabel')
        username_label.grid(column=1, row=1, sticky=tk.W, pady=5)
        self.username = ttk.Entry(mainframe, width=25)
        self.username.grid(column=2, row=1, sticky=(tk.W, tk.E))

        password_label = ttk.Label(mainframe, text="Password", font=("Helvetica", 12), style='Label.TLabel')
        password_label.grid(column=1, row=2, sticky=tk.W, pady=5)
        self.password = ttk.Entry(mainframe, width=25, show="*")
        self.password.grid(column=2, row=2, sticky=(tk.W, tk.E))

        #Login Buttons
        login_button = ttk.Button(mainframe, text="Login", command=self.login, style='Accent.TButton')
        login_button.grid(column=2, row=3, sticky=(tk.W, tk.E), pady=20)

        #Register
        register_button = ttk.Button(mainframe, text="Register", command=lambda: self.show_page("RegisterScreen"))
        register_button.grid(column=2, row=4, sticky=(tk.W, tk.E), pady=5)

        #Forgot Password
        forgot_password_button = ttk.Button(mainframe, text="Forgot Password", command=lambda: self.show_page("ForgotPasswordScreen"))
        forgot_password_button.grid(column=2, row=5, sticky=(tk.W, tk.E), pady=5)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        # Connect to the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Query the database for the username
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()

        # Check if the username exists in the database
        if result and hashlib.sha256(password.encode()).hexdigest() == result[1]:
            self.show_page("DashboardScreen")
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_page(self, page_name):
        if page_name == "DashboardScreen":
            self.destroy()
            DashboardScreen().mainloop()
        elif page_name == "RegisterScreen":
            self.destroy()
            RegisterScreen().mainloop()
        elif page_name == "ForgotPasswordScreen":
            self.destroy()
            ForgotPasswordScreen().mainloop()

if __name__ == "__main__":
    app = ChatbotGUI()

    #Styles
    style = ttk.Style()
    style.configure('MainFrame.TFrame', background='#2e2e2e')
    style.configure('Title.Tlabel', foreground='white', background='#2e2e2e')
    style.configure('Label.TLabel', foreground='white', background='#2e2e2e')
    style.configure('Accent.TButton', foreground='white', background='#4CAF50', font=("Helvetica", 12, "bold"))

    app.mainloop()