import sys
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from PyQt5.QtWidgets import QApplication
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
        self.qt_app = QApplication(sys.argv)

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Create a top frame for help button, logout button, and title
        top_frame = ttk.Frame(mainframe)
        top_frame.grid(column=0, row=0, sticky=(tk.W, tk.E))
        top_frame.columnconfigure(1, weight=1)  # Make the middle column expandable

        # Add logout button
        logout_button = ttk.Button(top_frame, text="Logout", command=self.logout)
        logout_button.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # Dashboard title in the center
        ttk.Label(top_frame, text="Dashboard", font=("Helvetica", 16)).grid(column=1, row=0)

        # Add help button to the right side
        help_button = ttk.Button(top_frame, text="Help", command=self.show_help)
        help_button.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)

        # Load and display the image
        self.load_image(mainframe)

        # Create a frame for buttons
        button_frame = ttk.Frame(mainframe)
        button_frame.grid(column=0, row=2, sticky=(tk.W, tk.E))

        # Create buttons
        buttons = [
            ("Budget Management", self.show_budget_management),
            ("Expense Tracking", self.show_expense_tracking),
            ("Savings Goals", self.show_savings_goals),
            ("Reports", self.show_reports),
            ("Settings", self.show_settings),
            ("ChatBot", self.show_chatbot),
        ]

        # Add buttons to the button frame
        for index, (text, command) in enumerate(buttons):
            button = ttk.Button(button_frame, text=text, command=command)
            button.grid(column=index, row=0, padx=5, pady=5)  # Add some padding between buttons

    def load_image(self, parent):
        # Load the image using PIL
        image = Image.open("Gemini_Generated_Image_qdqk0yqdqk0yqdqk.jfif")
        image = image.resize((200, 200), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        label = ttk.Label(parent, image=self.photo)
        label.grid(column=0, row=1, sticky=tk.W)  # Place image below the top frame

    def show_help(self):
        help_message = (
            "Welcome to the Financial Management Dashboard!\n\n"
            "To get the most out of this application, please follow these steps:\n\n"
            "1. Budget Management: Start by setting up your budget. Enter your income and planned expenses.\n"
            "2. Expense Tracking: Regularly log your daily expenses to keep track of your spending.\n"
            "3. Savings Goals: Set financial goals and track your progress towards achieving them.\n"
            "4. Reports: Generate and view reports to analyze your financial habits and progress.\n"
            "5. Settings: Customize the application settings to suit your preferences.\n\n"
            "Once you've familiarized yourself with these features, feel free to use the ChatBot for personalized financial advice.\n\n"
            "Remember, the more information you provide in the other sections, the better advice the ChatBot can offer!"
        )
        messagebox.showinfo("Help", help_message)

    def show_budget_management(self):
        self.destroy()
        BudgetManagementScreen().mainloop()

    def show_expense_tracking(self):
        self.withdraw()  # Hide the dashboard
        ExpenseTrackingScreen(self)  # Create and show the ExpenseTrackingScreen

    def show_savings_goals(self):
        self.withdraw()
        savings_screen = SavingsGoalsScreen(self)
        savings_screen.show()
        self.qt_app.exec_()
        self.deiconify()

    def show_reports(self):
        self.withdraw()
        reports_screen = ReportsScreen()
        reports_screen.show()
        self.qt_app.exec_()
        self.deiconify()

    def show_settings(self):
        self.withdraw()  # Hide the Tkinter window
        self.user_settings_screen = UserSettingsScreen(self)
        self.user_settings_screen.closed.connect(self.on_settings_closed)
        self.user_settings_screen.show()

    def on_settings_closed(self):
        self.deiconify()  # Show the Tkinter window again

    def show_chatbot(self):
        self.destroy()
        ChatBot().mainloop()

    def logout(self):
        self.destroy()
        import app
        app.show_login()

if __name__ == "__main__":
    app = DashboardScreen()
    app.mainloop()