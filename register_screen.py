import tkinter as tk
from datetime import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import hashlib
from typing import re
from dashboard_screen import DashboardScreen

class RegisterScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Register")
        self.geometry("800x600")
        self.create_widgets()
        self.configure(bg="black")

        # Connect to the database
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users
                    (first_name TEXT, last_name TEXT, email TEXT, age INTEGER, username TEXT, password TEXT, 
                     security_question1 TEXT, security_answer1 TEXT, 
                     security_question2 TEXT, security_answer2 TEXT,
                     security_question3 TEXT, security_answer3 TEXT,
                     is_robot BOOLEAN)
                ''')
        self.conn.commit()

    def create_widgets(self):
        # Main Frame
        mainframe = ttk.Frame(self, padding="40 40 40 40", style='MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(mainframe, text="Join Our Community", font=("Helvetica", 28, "bold"),
                                style='Title.TLabel')
        title_label.grid(column=1, row=0, columnspan=2, pady=20)

        # Subtitle
        subtitle_label = ttk.Label(mainframe, text="Unlock a world of opportunities and connections.",
                                   font=("Helvetica", 16), style='Subtitle.TLabel')
        subtitle_label.grid(column=1, row=1, columnspan=2, pady=10)

        # First Name Label
        first_name_label = ttk.Label(mainframe, text="First Name:", font=("Helvetica", 14), style='Label.TLabel')
        first_name_label.grid(column=1, row=2, sticky=tk.W, pady=10)
        self.first_name = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.first_name.grid(column=2, row=2, sticky=(tk.W, tk.E), pady=10)

        # Last Name Label
        last_name_label = ttk.Label(mainframe, text="Last Name:", font=("Helvetica", 14), style='Label.TLabel')
        last_name_label.grid(column=1, row=3, sticky=tk.W, pady=10)
        self.last_name = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.last_name.grid(column=2, row=3, sticky=(tk.W, tk.E), pady=10)

        # Email Label
        email_label = ttk.Label(mainframe, text="Email:", font=("Helvetica", 14), style='Label.TLabel')
        email_label.grid(column=1, row=4, sticky=tk.W, pady=10)
        self.email = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.email.grid(column=2, row=4, sticky=(tk.W, tk.E), pady=10)

        # Age Label
        age_label = ttk.Label(mainframe, text="Age:", font=("Helvetica", 14), style='Label.TLabel')
        age_label.grid(column=1, row=5, sticky=tk.W, pady=10)
        self.age = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.age.grid(column=2, row=5, sticky=(tk.W, tk.E), pady=10)

        # Username Label
        username_label = ttk.Label(mainframe, text="Username:", font=("Helvetica", 14), style='Label.TLabel')
        username_label.grid(column=1, row=6, sticky=tk.W, pady=10)
        self.username = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.username.grid(column=2, row=6, sticky=(tk.W, tk.E), pady=10)

        # Password Label
        password_label = ttk.Label(mainframe, text="Password:", font=("Helvetica", 14), style='Label.TLabel')
        password_label.grid(column=1, row=7, sticky=tk.W, pady=10)
        self.password = ttk.Entry(mainframe, width=30, show="*", font=("Helvetica", 12))
        self.password.grid(column=2, row=7, sticky=(tk.W, tk.E), pady=10)

        # Confirm Password Label
        confirm_password_label = ttk.Label(mainframe, text="Confirm Password:", font=("Helvetica", 14),
                                           style='Label.TLabel')
        confirm_password_label.grid(column=1, row=8, sticky=tk.W, pady=10)
        self.confirm_password = ttk.Entry(mainframe, width=30, show="*", font=("Helvetica", 12))
        self.confirm_password.grid(column=2, row=8, sticky=(tk.W, tk.E), pady=10)

        # Security Question 1 Label
        security_question1_label = ttk.Label(mainframe, text="Security Question 1:", font=("Helvetica", 14),
                                             style='Label.TLabel')
        security_question1_label.grid(column=1, row=9, sticky=tk.W, pady=10)
        self.security_question1 = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.security_question1.grid(column=2, row=9, sticky=(tk.W, tk.E), pady=10)

        # Security Answer 1 Label
        security_answer1_label = ttk.Label(mainframe, text="Security Answer 1:", font=("Helvetica", 14),
                                           style='Label.TLabel')
        security_answer1_label.grid(column=1, row=10, sticky=tk.W, pady=10)
        self.security_answer1 = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.security_answer1.grid(column=2, row=10, sticky=(tk.W, tk.E), pady=10)

        # Security Question 2 Label
        security_question2_label = ttk.Label(mainframe, text="Security Question 2:", font=("Helvetica", 14),
                                             style='Label.TLabel')
        security_question2_label.grid(column=1, row=11, sticky=tk.W, pady=10)
        self.security_question2 = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.security_question2.grid(column=2, row=11, sticky=(tk.W, tk.E), pady=10)

        # Security Answer 2 Label
        security_answer2_label = ttk.Label(mainframe, text="Security Answer 2:", font=("Helvetica", 14),
                                           style='Label.TLabel')
        security_answer2_label.grid(column=1, row=12, sticky=tk.W, pady=10)
        self.security_answer2 = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.security_answer2.grid(column=2, row=12, sticky=(tk.W, tk.E), pady=10)

        # Security Question 3 Label
        security_question3_label = ttk.Label(mainframe, text="Security Question 3:", font=("Helvetica", 14),
                                             style='Label.TLabel')
        security_question3_label.grid(column=1, row=13, sticky=tk.W, pady=10)
        self.security_question3 = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.security_question3.grid(column=2, row=13, sticky=(tk.W, tk.E), pady=10)

        # Security Answer 3 Label
        security_answer3_label = ttk.Label(mainframe, text="Security Answer 3:", font=("Helvetica", 14),
                                           style='Label.TLabel')
        security_answer3_label.grid(column=1, row=14, sticky=tk.W, pady=10)
        self.security_answer3 = ttk.Entry(mainframe, width=30, font=("Helvetica", 12))
        self.security_answer3.grid(column=2, row=14, sticky=(tk.W, tk.E), pady=10)

        # Register Button
        register_button = ttk.Button(mainframe, text="Join Now", command=self.save_data, style='Accent.TButton')
        register_button.grid(column=2, row=15, sticky=(tk.W, tk.E), pady=20)

        # Back Button
        back_button = ttk.Button(mainframe, text="Back", command=self.close_window, style='TButton')
        back_button.grid(column=1, row=15, sticky=(tk.W, tk.E), pady=20)

    def save_data(self):
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        age = self.age.get()
        username = self.username.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()
        security_question1 = self.security_question1.get()
        security_answer1 = self.security_answer1.get()
        security_question2 = self.security_question2.get()
        security_answer2 = self.security_answer2.get()
        security_question3 = self.security_question3.get()
        security_answer3 = self.security_answer3.get()

        # Validate password requirements
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}$'
        if not re.match(password_pattern, password):
            messagebox.showerror("Error",
                                 "Password must be at least 7 characters long and include at least one lowercase letter, one uppercase letter, one number, and one special character.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Check if the user is above 18 years old
        if int(age) < 18:
            messagebox.showerror("Error", "You must be at least 18 years old to register.")
            return


        # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Insert the data into the database
        self.cursor.execute('''
                    INSERT INTO users (first_name, last_name, email, age, username, password, 
                                      security_question1, security_answer1, 
                                      security_question2, security_answer2, 
                                      security_question3, security_answer3,
                                      is_robot)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (first_name, last_name, email, age, username, password_hash,
                      security_question1, security_answer1,
                      security_question2, security_answer2,
                      security_question3, security_answer3,
                      False))
        self.conn.commit()

        # Clear the text fields
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.age.delete(0, tk.END)
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.confirm_password.delete(0, tk.END)
        self.security_question1.delete(0, tk.END)
        self.security_answer1.delete(0, tk.END)
        self.security_question2.delete(0, tk.END)
        self.security_answer2.delete(0, tk.END)
        self.security_question3.delete(0, tk.END)
        self.security_answer3.delete(0, tk.END)

        messagebox.showinfo("Success", "Registration successful!")
        self.destroy()
        DashboardScreen().mainloop()

    def close_window(self):
        self.destroy()