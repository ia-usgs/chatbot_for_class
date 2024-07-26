import tkinter as tk
from tkinter import ttk, messagebox

class AdminScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Admin Dashboard")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        mainframe = ttk.Frame(self, padding="20", style='MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(mainframe, text="Admin Dashboard", font=("Helvetica", 20, "bold"), foreground="white").grid(column=1, row=0, columnspan=2, pady=20)

        # Button to view users
        view_users_button = ttk.Button(mainframe, text="View Users", command=self.view_users, style='Accent.TButton')
        view_users_button.grid(column=1, row=1, pady=10, sticky=tk.E)

        # Button to view reports
        view_reports_button = ttk.Button(mainframe, text="View Financial Reports", command=self.view_reports, style='Accent.TButton')
        view_reports_button.grid(column=1, row=2, pady=10, sticky=tk.E)

        # Button to manage settings
        manage_settings_button = ttk.Button(mainframe, text="Manage Settings", command=self.manage_settings, style='Accent.TButton')
        manage_settings_button.grid(column=1, row=3, pady=10, sticky=tk.E)

    def configure_style(self):
        # Configure styles for dark theme
        style = ttk.Style()
        style.configure('MainFrame.TFrame', background='black')
        style.configure('Accent.TButton', background='#555', foreground='white', font=("Helvetica", 12))
        style.map('Accent.TButton', background=[('active', '#777')], foreground=[('active', 'black')])

    def view_users(self):
        # Placeholder for user viewing logic
        messagebox.showinfo("View Users", "This feature will display a list of users.")

    def view_reports(self):
        # Placeholder for report viewing logic
        messagebox.showinfo("View Reports", "This feature will display financial reports.")

    def manage_settings(self):
        # Placeholder for settings management logic
        messagebox.showinfo("Manage Settings", "This feature will allow admin to manage application settings.")

if __name__ == "__main__":
    app = AdminScreen()
    app.mainloop()

