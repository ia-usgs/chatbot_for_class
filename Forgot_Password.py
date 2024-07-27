import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
from dashboard_screen import DashboardScreen

#Forgot Password Screen
class ForgotPasswordScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Forgot Password")
        self.geometry("400x300")
        self.create_widgets()
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

    def create_widgets(self):
        self.mainframe = ttk.Frame(self, padding="20 20 20 20")
        self.mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        title_label = ttk.Label(self.mainframe, text="Reset your password", font=("Helvetica", 16, "bold"))
        title_label.grid(column=1, row=0, columnspan=2, pady=10)

        username_label = ttk.Label(self.mainframe, text="Username", font=("Helvetica", 12))
        username_label.grid(column=1, row=1, sticky=tk.W, pady=5)
        self.username = ttk.Entry(self.mainframe, width=25)
        self.username.grid(column=2, row=1, sticky=(tk.W, tk.E))

        new_password_label = ttk.Label(self.mainframe, text="New Password", font=("Helvetica", 12))
        new_password_label.grid(column=1, row=2, sticky=tk.W, pady=5)
        self.new_password = ttk.Entry(self.mainframe, width=25, show="*")
        self.new_password.grid(column=2, row=2, sticky=(tk.W, tk.E))

        reset_button = ttk.Button(self.mainframe, text="Reset Password", command=self.reset_password)
        reset_button.grid(column=2, row=3, sticky=(tk.W, tk.E), pady=20)

        back_button = ttk.Button(self.mainframe, text="Back", command=self.destroy)
        back_button.grid(column=2, row=4, sticky=(tk.W, tk.E), pady=5)

    def reset_password(self):
        username = self.username.get()
        new_password = self.new_password.get()
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()

        self.cursor.execute('UPDATE users SET password = ? WHERE username = ?', (hashed_password, username))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            messagebox.showinfo("Success", "Password reset successfully.")
            self.destroy()
        else:
            messagebox.showerror("Error", "Username not found.")
