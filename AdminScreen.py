import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class AdminScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Admin Dashboard")
        self.geometry("800x600")
        self.create_widgets()
        self.configure_style()

    def create_widgets(self):
        # Create main frame
        mainframe = ttk.Frame(self, padding="20", style='MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Admin Dashboard", font=("Helvetica", 20, "bold"), foreground="white").grid(column=0, row=0, columnspan=2, pady=20)

        # Button to view user count
        view_users_button = ttk.Button(mainframe, text="View User Count", command=self.view_user_count, style='Accent.TButton')
        view_users_button.grid(column=0, row=1, pady=10, padx=10, sticky=tk.W)

        # Button to view user issues
        view_issues_button = ttk.Button(mainframe, text="View User Issues", command=self.view_user_issues, style='Accent.TButton')
        view_issues_button.grid(column=1, row=1, pady=10, padx=10, sticky=tk.W)

        # Button to view bug reports
        view_bugs_button = ttk.Button(mainframe, text="View Bug Reports", command=self.view_bug_reports, style='Accent.TButton')
        view_bugs_button.grid(column=0, row=2, pady=10, padx=10, sticky=tk.W)

        # Text widget to display information
        self.info_text = tk.Text(mainframe, height=15, width=70, bg='#2e2e2e', fg='white')
        self.info_text.grid(column=0, row=3, columnspan=2, pady=20, padx=10)

        # Logout button
        logout_button = ttk.Button(mainframe, text="Logout", command=self.logout, style='Accent.TButton')
        logout_button.grid(column=1, row=4, pady=10, padx=10, sticky=tk.E)

    def configure_style(self):
        style = ttk.Style()
        style.configure('MainFrame.TFrame', background='#1e1e1e')
        style.configure('Accent.TButton', background='#555', foreground='white', font=("Helvetica", 12))
        style.map('Accent.TButton', background=[('active', '#777')], foreground=[('active', 'white')])

    def view_user_count(self):
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, f"Total number of users: {count}")
            conn.close()
        except sqlite3.Error as e:
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, f"An error occurred: {e}")

    def view_user_issues(self):
        # This is a placeholder. You'll need to implement a system to track user issues.
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "User issues tracking system not implemented yet.")

    def view_bug_reports(self):
        # This is a placeholder. You'll need to implement a system to track bug reports.
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "Bug reporting system not implemented yet.")

    def logout(self):
        self.destroy()
        # Here you would typically return to the login screen
        # For example: LoginScreen().mainloop()

if __name__ == "__main__":
    app = AdminScreen()
    app.mainloop()
