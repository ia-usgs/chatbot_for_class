import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import hashlib
from dashboard_screen import DashboardScreen

class RegisterScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Register")
        self.geometry("800x600")
        self.create_widgets()
        
        # Connect to the database
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        
        # Create the table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (username TEXT, password TEXT)
        ''')
        self.conn.commit()

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

        register_button = ttk.Button(mainframe, text="Register", command=self.save_data)
        register_button.grid(column=2, row=3, sticky=tk.W)

    def save_data(self):
        username = self.username.get()
        password = self.password.get()

        # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Insert the data into the database
        self.cursor.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', (username, password_hash))
        self.conn.commit()

        # Clear the text fields
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)

        messagebox.showinfo("Success", "Registration successful!")

        # Navigate to DashboardScreen
        self.show_page("DashboardScreen")

    def show_page(self, page_name):
        if page_name == "DashboardScreen":
            self.destroy()
            DashboardScreen().mainloop()
