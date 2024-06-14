from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont

class ExpenseTrackingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Expense Tracking")
        self.setGeometry(300, 300, 800, 600)
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        label = QLabel("Expense Tracking")
        label.setFont(QFont("Helvetica", 16))
        grid.addWidget(label, 0, 0)

        # Add widgets for expense tracking here
        pass