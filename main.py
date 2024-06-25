import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
import sqlite3
from dashboard_screen import DashboardScreen
from register_screen import RegisterScreen
import sv_ttk

class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Financial Chatbot")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Username").grid(column=1, row=1, sticky=tk.W)
        self.username = ttk.Entry(mainframe, width=25)
        self.username.grid(column=2, row=1, sticky=(tk.W, tk.E))

        ttk.Label(mainframe, text="Password").grid(column=1, row=2, sticky=tk.W)
        self.password = ttk.Entry(mainframe, width=25, show="*")
        self.password.grid(column=2, row=2, sticky=(tk.W, tk.E))

        login_button = ttk.Button(mainframe, text="Login", command=self.login)
        login_button.grid(column=2, row=3, sticky=tk.W)

        register_button = ttk.Button(mainframe, text="Register", command=lambda: self.show_page("RegisterScreen"))
        register_button.grid(column=2, row=4, sticky=tk.W)

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

if __name__ == "__main__":
    app = ChatbotGUI()
    sv_ttk.set_theme("dark")
    app.mainloop()