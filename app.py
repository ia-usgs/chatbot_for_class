import tkinter as tk
from tkinter import ttk

class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Financial Chatbot")
        self.geometry("800x600")
        
        # Initialize frames for each screen
        self.frames = {}
        for F in (LoginScreen, DashboardScreen, BudgetManagementScreen, ExpenseTrackingScreen, 
                  SavingsGoalsScreen, ReportsScreen, UserSettingsScreen, AdminDashboardScreen, 
                  UserManagementScreen, SystemConfigurationScreen):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("LoginScreen")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Username").grid(row=0, column=0)
        self.username = tk.Entry(self)
        self.username.grid(row=0, column=1)
        
        tk.Label(self, text="Password").grid(row=1, column=0)
        self.password = tk.Entry(self, show="*")
        self.password.grid(row=1, column=1)
        
        tk.Button(self, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)
        tk.Button(self, text="Register", command=lambda: self.controller.show_frame("RegisterScreen")).grid(row=3, column=0, columnspan=2)
    
    def login(self):
        # Placeholder for login logic
        self.controller.show_frame("DashboardScreen")

class DashboardScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Dashboard", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(self, text="Budget Management", command=lambda: self.controller.show_frame("BudgetManagementScreen")).pack(pady=5)
        tk.Button(self, text="Expense Tracking", command=lambda: self.controller.show_frame("ExpenseTrackingScreen")).pack(pady=5)
        tk.Button(self, text="Savings Goals", command=lambda: self.controller.show_frame("SavingsGoalsScreen")).pack(pady=5)
        tk.Button(self, text="Reports", command=lambda: self.controller.show_frame("ReportsScreen")).pack(pady=5)
        tk.Button(self, text="Settings", command=lambda: self.controller.show_frame("UserSettingsScreen")).pack(pady=5)

class BudgetManagementScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Budget Management", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for budget management

class ExpenseTrackingScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Expense Tracking", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for expense tracking

class SavingsGoalsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Savings Goals", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for savings goals

class ReportsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Reports", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for reports

class UserSettingsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="User Settings", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for user settings

class AdminDashboardScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="Admin Dashboard", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for admin dashboard

class UserManagementScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="User Management", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for user management

class SystemConfigurationScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self, text="System Configuration", font=("Helvetica", 16)).pack(pady=10)
        # Add more widgets for system configuration

if __name__ == "__main__":
    app = ChatbotGUI()
    app.mainloop()
