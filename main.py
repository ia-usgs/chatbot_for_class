import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import bcrypt
from PyQt5.QtGui import QFont
from dashboard_screen import DashboardScreen
from register_screen import RegisterScreen
import sqlite3

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
        # Connect to the database
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

        # Query the database for the username
        self.cursor.execute('''
            SELECT * FROM budget
            WHERE username = ?
        ''', (username,))

        # Fetch the result
        result = self.cursor.fetchone()

        # Check if the username exists in the database
        if result:
            # Check the password
            if bcrypt.checkpw(password.encode('utf-8'), result[1]):
                self.showPage("DashboardScreen")
                self.close()
            else:
                print("Invalid password")
        else:
            print("Invalid username")

    def showPage(self, pageName):
        if pageName == "DashboardScreen":
            self.dashboard = DashboardScreen()
            self.dashboard.show()
        elif pageName == "RegisterScreen":
            self.register = RegisterScreen()
            self.register.show()
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = ChatbotGUI()
    gui.show()
    sys.exit(app.exec_())