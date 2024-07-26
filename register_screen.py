import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import hashlib
import sqlite3
import os

class RegisterScreen(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Check if theme 'forest-dark' is already loaded
        if 'forest-dark' not in ttk.Style().theme_names():
            self.tk.call('source', 'forest-dark.tcl')
            ttk.Style().theme_use('forest-dark')

        self.title("Register")
        self.geometry("800x600")
        self.configure(bg="black")
        self.create_widgets()

        # Connect to the database
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

        # Drop the table if it exists (for testing, remove this in production)
        self.cursor.execute('DROP TABLE IF EXISTS users')

        # Create the table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                age INTEGER,
                username TEXT,
                salt,
                password TEXT,
                security_question1 TEXT,
                security_answer1 TEXT,
                security_question2 TEXT,
                security_answer2 TEXT,
                security_question3 TEXT,
                security_answer3 TEXT,
                is_robot BOOLEAN
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="20 20 20 20", style='MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(mainframe, text="Register", font=("Helvetica", 20, "bold"), style='Title.TLabel')
        title_label.grid(column=1, row=0, columnspan=2, pady=20)

        # First Name
        first_name_label = ttk.Label(mainframe, text="First Name", font=("Helvetica", 12), style='Label.TLabel')
        first_name_label.grid(column=1, row=1, sticky=tk.W, pady=5)
        self.first_name = ttk.Entry(mainframe, width=25)
        self.first_name.grid(column=2, row=1, sticky=(tk.W, tk.E))

        # Last Name
        last_name_label = ttk.Label(mainframe, text="Last Name", font=("Helvetica", 12), style='Label.TLabel')
        last_name_label.grid(column=1, row=2, sticky=tk.W, pady=5)
        self.last_name = ttk.Entry(mainframe, width=25)
        self.last_name.grid(column=2, row=2, sticky=(tk.W, tk.E))

        # Email
        email_label = ttk.Label(mainframe, text="Email", font=("Helvetica", 12), style='Label.TLabel')
        email_label.grid(column=1, row=3, sticky=tk.W, pady=5)
        self.email = ttk.Entry(mainframe, width=25)
        self.email.grid(column=2, row=3, sticky=(tk.W, tk.E))

        # Age
        age_label = ttk.Label(mainframe, text="Age", font=("Helvetica", 12), style='Label.TLabel')
        age_label.grid(column=1, row=4, sticky=tk.W, pady=5)
        self.age = ttk.Entry(mainframe, width=25)
        self.age.grid(column=2, row=4, sticky=(tk.W, tk.E))

        # Username
        username_label = ttk.Label(mainframe, text="Username", font=("Helvetica", 12), style='Label.TLabel')
        username_label.grid(column=1, row=5, sticky=tk.W, pady=5)
        self.username = ttk.Entry(mainframe, width=25)
        self.username.grid(column=2, row=5, sticky=(tk.W, tk.E))

        # Password
        password_label = ttk.Label(mainframe, text="Password", font=("Helvetica", 12), style='Label.TLabel')
        password_label.grid(column=1, row=6, sticky=tk.W, pady=5)
        self.password = ttk.Entry(mainframe, width=25, show="*")
        self.password.grid(column=2, row=6, sticky=(tk.W, tk.E))

        # Confirm Password
        confirm_password_label = ttk.Label(mainframe, text="Confirm Password", font=("Helvetica", 12), style='Label.TLabel')
        confirm_password_label.grid(column=1, row=7, sticky=tk.W, pady=5)
        self.confirm_password = ttk.Entry(mainframe, width=25, show="*")
        self.confirm_password.grid(column=2, row=7, sticky=(tk.W, tk.E))

        # Security Questions
        security_question1_label = ttk.Label(mainframe, text="Security Question 1", font=("Helvetica", 12), style='Label.TLabel')
        security_question1_label.grid(column=1, row=8, sticky=tk.W, pady=5)
        self.security_question1 = ttk.Combobox(mainframe, values=[
            "What is your mother's maiden name?",
            "What city were you born in?",
            "What is your favorite movie?",
            "What was the name of your first pet?"
        ], state="readonly", width=50)
        self.security_question1.grid(column=2, row=8, sticky=(tk.W, tk.E))

        security_answer1_label = ttk.Label(mainframe, text="Answer", font=("Helvetica", 12), style='Label.TLabel')
        security_answer1_label.grid(column=1, row=9, sticky=tk.W, pady=5)
        self.security_answer1 = ttk.Entry(mainframe, width=25)
        self.security_answer1.grid(column=2, row=9, sticky=(tk.W, tk.E))

        security_question2_label = ttk.Label(mainframe, text="Security Question 2", font=("Helvetica", 12), style='Label.TLabel')
        security_question2_label.grid(column=1, row=10, sticky=tk.W, pady=5)
        self.security_question2 = ttk.Combobox(mainframe, values=[
            "What is your favorite book?",
            "Who is your favorite musician?",
            "What is your dream job?",
            "What is the name of your favorite teacher?"
        ], state="readonly", width=50)
        self.security_question2.grid(column=2, row=10, sticky=(tk.W, tk.E))

        security_answer2_label = ttk.Label(mainframe, text="Answer", font=("Helvetica", 12), style='Label.TLabel')
        security_answer2_label.grid(column=1, row=11, sticky=tk.W, pady=5)
        self.security_answer2 = ttk.Entry(mainframe, width=25)
        self.security_answer2.grid(column=2, row=11, sticky=(tk.W, tk.E))

        security_question3_label = ttk.Label(mainframe, text="Security Question 3", font=("Helvetica", 12), style='Label.TLabel')
        security_question3_label.grid(column=1, row=12, sticky=tk.W, pady=5)
        self.security_question3 = ttk.Combobox(mainframe, values=[
            "What is your favorite food?",
            "What is your biggest fear?",
            "Where did you go on your first vacation?",
            "What is your favorite color?"
        ], state="readonly", width=50)
        self.security_question3.grid(column=2, row=12, sticky=(tk.W, tk.E))

        security_answer3_label = ttk.Label(mainframe, text="Answer", font=("Helvetica", 12), style='Label.TLabel')
        security_answer3_label.grid(column=1, row=13, sticky=tk.W, pady=5)
        self.security_answer3 = ttk.Entry(mainframe, width=25)
        self.security_answer3.grid(column=2, row=13, sticky=(tk.W, tk.E))

        # Back Button
        back_button = ttk.Button(mainframe, text="Back", command=self.back_to_main)
        back_button.grid(column=1, row=14, sticky=(tk.W, tk.E), pady=20)

        # Register Button
        register_button = ttk.Button(mainframe, text="Register", command=self.save_data)
        register_button.grid(column=2, row=14, sticky=(tk.W, tk.E), pady=20)

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

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email format.")
            return

        # Validate password strength
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{7,}$'
        if not re.match(password_pattern, password):
            messagebox.showerror("Error",
                                "Password must be at least 7 characters long and include at least one lowercase letter, one uppercase letter, one number, and one special character.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # User must be above 18 years old
        if int(age) < 18:
            messagebox.showerror("Error", "You must be at least 18 years old to register.")
            return

        # Generate a random salt
        salt = os.urandom(16).hex()

        # Hash the password with the salt
        password_hash = hashlib.sha256((salt + password).encode()).hexdigest()

        # Insert the data into the database
        self.cursor.execute('''
                    INSERT INTO users (first_name, last_name, email, age, username, password, 
                                    salt, security_question1, security_answer1, 
                                    security_question2, security_answer2, 
                                    security_question3, security_answer3,
                                    is_robot)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (first_name, last_name, email, age, username, password_hash,
                    salt, security_question1, security_answer1,
                    security_question2, security_answer2,
                    security_question3, security_answer3,
                    False))
        self.conn.commit()

        # Clear the text fields
        self.clear_fields()

        messagebox.showinfo("Success", "Registration successful!")

        self.back_to_main()

    def clear_fields(self):
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.age.delete(0, tk.END)
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.confirm_password.delete(0, tk.END)
        self.security_answer1.delete(0, tk.END)
        self.security_answer2.delete(0, tk.END)
        self.security_answer3.delete(0, tk.END)

    def back_to_main(self):
        self.destroy()  # Close the RegisterScreen window
        self.main_window.deiconify()  # Show the main window
