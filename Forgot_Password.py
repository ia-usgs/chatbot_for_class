import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
from dashboard_screen import DashboardScreen

#Forgot Password Screen
class ForgotPasswordScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Forgot Password")
        self.geometry("400x300")
        self.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="20 20 20 20", style='MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Forgot Password", font=("Helvetica", 20, "bold"), style='Title.TLabel').grid(column=1, row=0, columnspan=2, pady=20)

        ttk.Label(mainframe, text="Enter your username:", font=("Helvetica", 12), style='Label.TLabel').grid(column=1, row=1, sticky=tk.W, pady=5)
        self.username = ttk.Entry(mainframe, width=25)
        self.username.grid(column=2, row=1, sticky=(tk.W, tk.E))

        reset_button = ttk.Button(mainframe, text="Reset Password", command=self.reset_password, style='Accent.TButton')
        reset_button.grid(column=2, row=2, sticky=(tk.W, tk.E), pady=20)

    def reset_password(self):
        username = self.username.get()
        # Logic to reset the password
        messagebox.showinfo("Info", f"Password reset instructions sent to {username}")

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

        messagebox.showinfo("Success", "Password reset is successful!")

        # Navigate to DashboardScreen
        self.show_page("DashboardScreen")

    def show_page(self, page_name):
        if page_name == "DashboardScreen":
            self.destroy()
            DashboardScreen().mainloop()