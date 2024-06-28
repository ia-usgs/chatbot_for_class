import tkinter as tk
from tkinter import ttk
from budget_management_screen import BudgetManagementScreen
from expense_tracking_screen import ExpenseTrackingScreen
from reports_screen import ReportsScreen
from savings_goals_screen import SavingsGoalsScreen
from user_settings_screen import UserSettingsScreen
from ChatBot import ChatBot

class DashboardScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Dashboard")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Dashboard", font=("Helvetica", 16)).grid(column=0, row=0, sticky=tk.W)

        self.create_button(mainframe, "Budget Management", self.show_budget_management).grid(column=0, row=1, sticky=tk.W)
        self.create_button(mainframe, "Expense Tracking", self.show_expense_tracking).grid(column=0, row=2, sticky=tk.W)
        self.create_button(mainframe, "Savings Goals", self.show_savings_goals).grid(column=0, row=3, sticky=tk.W)
        self.create_button(mainframe, "Reports", self.show_reports).grid(column=0, row=4, sticky=tk.W)
        self.create_button(mainframe, "Settings", self.show_settings).grid(column=0, row=5, sticky=tk.W)
        self.create_button(mainframe, "ChatBot", self.show_chatbot).grid(column=0, row=6, sticky=tk.W)

    def create_button(self, parent, text, command):
        return ttk.Button(parent, text=text, command=command)

    def show_budget_management(self):
        self.destroy()
        BudgetManagementScreen().mainloop()

    def show_expense_tracking(self):
        self.destroy()
        ExpenseTrackingScreen().mainloop()

    def show_savings_goals(self):
        self.destroy()
        SavingsGoalsScreen().mainloop()

    def show_reports(self):
        self.destroy()
        ReportsScreen().mainloop()

    def show_settings(self):
        self.destroy()
        UserSettingsScreen().mainloop()

    def show_chatbot(self):
        self.destroy()
        ChatBot().mainloop()
