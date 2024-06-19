from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit
import sqlite3
import csv

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
        self.income_input = QLineEdit()
        grid.addWidget(self.income_input, 1, 1)

        expense_label = QLabel("Expenses:")
        grid.addWidget(expense_label, 2, 0)
        self.expense_input = QLineEdit()
        grid.addWidget(self.expense_input, 2, 1)

        save_button = QPushButton("Save")
        grid.addWidget(save_button, 3, 0, 1, 2)
        
        save_button.clicked.connect(self.save_data)

        # Connect to the database
        self.conn = sqlite3.connect('budget.db')
        self.cursor = self.conn.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS budget
            (income REAL, expenses REAL)
        ''')

    def save_data(self):
        try:
            income = float(self.income_input.text())
            expenses = float(self.expense_input.text())

            # Create a CSV file
            with open('budget.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([income, expenses])

            # Clear the text fields
            self.income_input.clear()
            self.expense_input.clear()

            # Provide user feedback
            QMessageBox.information(self, "Success", "Data saved successfully!")
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input. Please enter valid numbers for income and expenses.")
        except Exception as e:
            QMessageBox.critical(self, "Error", "An error occurred: " + str(e))