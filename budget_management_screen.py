from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit

class BudgetManagementScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Budget Management")
        self.setGeometry(300, 300, 800, 600)
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        label = QLabel("Budget Management")
        label.setFont(QFont("Helvetica", 16))
        grid.addWidget(label, 0, 0, 1, 2)

        income_label = QLabel("Income:")
        grid.addWidget(income_label, 1, 0)
        income_input = QLineEdit()
        grid.addWidget(income_input, 1, 1)

        expense_label = QLabel("Expenses:")
        grid.addWidget(expense_label, 2, 0)
        expense_input = QLineEdit()
        grid.addWidget(expense_input, 2, 1)

        save_button = QPushButton("Save")
        grid.addWidget(save_button, 3, 0, 1, 2)