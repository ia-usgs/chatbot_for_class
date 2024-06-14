import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import hashlib
import getpass
import os
import bcrypt
from PyQt5.QtGui import QFont

class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Financial Chatbot")
        self.setGeometry(300, 300, 800, 600)
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel("Username"), 0, 0)
        self.username = QLineEdit()
        grid.addWidget(self.username, 0, 1)

        grid.addWidget(QLabel("Password"), 1, 0)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        grid.addWidget(self.password, 1, 1)

        loginButton = QPushButton("Login")
        loginButton.clicked.connect(self.login)
        grid.addWidget(loginButton, 2, 0, 1, 2)

        registerButton = QPushButton("Register")
        registerButton.clicked.connect(lambda: self.showPage("RegisterScreen"))
        grid.addWidget(registerButton, 3, 0, 1, 2)

    def login(self):
        username = self.username.text()
        password = self.password.text()
        # Generate the hash for the password
        hashed_password = bcrypt.hashpw(b'123', bcrypt.gensalt())

        # Check the password
        if username == "admin" and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            self.showPage("DashboardScreen")
            self.close() # this makes it so that it closes the window
            
        else:
            print("Invalid username or password")

    def showPage(self, pageName):
        if pageName == "DashboardScreen":
            self.dashboard = DashboardScreen()
            self.dashboard.show()
        #elif pageName == "RegisterScreen":
            #self.register = RegisterScreen()
            #self.register.show()

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

    def showPage(self, pageName):
        #if pageName == "BudgetManagementScreen":
            #self.budget_management = BudgetManagementScreen()
            #self.budget_management.show()
        #elif pageName == "ExpenseTrackingScreen":
           # self.expense_tracking = ExpenseTrackingScreen()
            #self.expense_tracking.show()
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = ChatbotGUI()
    gui.show()
    sys.exit(app.exec_())