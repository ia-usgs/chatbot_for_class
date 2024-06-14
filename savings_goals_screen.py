from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont

class SavingsGoalsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Savings Goals")
        self.setGeometry(300, 300, 800, 600)
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        label = QLabel("Savings Goals")
        label.setFont(QFont("Helvetica", 16))
        grid.addWidget(label, 0, 0)

        # Add widgets for savings goals here
        pass