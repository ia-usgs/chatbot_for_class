from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from dashboard_screen import DashboardScreen

class RegisterScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Register")
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

        registerButton = QPushButton("Register")
        registerButton.clicked.connect(lambda: self.showPage("DashboardScreen"))
        grid.addWidget(registerButton, 2, 0, 1, 2)

    def showPage(self, pageName):
        if pageName == "DashboardScreen":
            self.dashboard = DashboardScreen()
            self.dashboard.show()
            self.close()

    