from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from budget_management_screen import BudgetManagementScreen
from expense_tracking_screen import ExpenseTrackingScreen
from reports_screen import ReportsScreen
from savings_goals_screen import SavingsGoalsScreen
from user_settings_screen import UserSettingsScreen
from ChatBot import ChatBot

class DashboardScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dashboard")
        self.setGeometry(300, 300, 800, 600)
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        label = QLabel("Dashboard")
        label.setFont(QFont("Helvetica", 16))
        grid.addWidget(label, 0, 0)

        button = QPushButton("Budget Management")
        button.clicked.connect(lambda: self.showPage("BudgetManagementScreen"))
        grid.addWidget(button, 1, 0)

        button = QPushButton("Expense Tracking")
        button.clicked.connect(lambda: self.showPage("ExpenseTrackingScreen"))
        grid.addWidget(button, 2, 0)

        button = QPushButton("Savings Goals")
        button.clicked.connect(lambda: self.showPage("SavingsGoalsScreen"))
        grid.addWidget(button, 3, 0)

        button = QPushButton("Reports")
        button.clicked.connect(lambda: self.showPage("ReportsScreen"))
        grid.addWidget(button, 4, 0)

        button = QPushButton("Settings")
        button.clicked.connect(lambda: self.showPage("UserSettingsScreen"))
        grid.addWidget(button, 5, 0)
        
        button = QPushButton("ChatBot")
        button.clicked.connect(lambda: self.showPage("ChatBot"))
        grid.addWidget(button, 6, 0)

    def showPage(self, pageName):
        if pageName == "BudgetManagementScreen":
            self.budget_management = BudgetManagementScreen()
            self.budget_management.show()
        elif pageName == "ExpenseTrackingScreen":
            self.expense_tracking = ExpenseTrackingScreen()
            self.expense_tracking.show()
        elif pageName == "SavingsGoalsScreen":
            self.expense_tracking = SavingsGoalsScreen()
            self.expense_tracking.show()
        elif pageName == "ReportsScreen":
            self.expense_tracking = ReportsScreen()
            self.expense_tracking.show()
        elif pageName == "UserSettingsScreen":
            self.expense_tracking = UserSettingsScreen()
            self.expense_tracking.show()
        elif pageName == "ChatBot":
            self.expense_tracking = ChatBot()
            self.expense_tracking.show()
            