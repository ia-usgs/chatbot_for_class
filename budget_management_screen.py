from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit
import sqlite3
import csv
import pandas as pd

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

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Income"))
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Expenses"))
        grid.addWidget(self.table_widget, 1, 0, 1, 2)

        income_label = QLabel("Income:")
        grid.addWidget(income_label, 2, 0)
        self.income_input = QLineEdit()
        grid.addWidget(self.income_input, 2, 1)

        expense_label = QLabel("Expenses:")
        grid.addWidget(expense_label, 3, 0)
        self.expense_input = QLineEdit()
        grid.addWidget(self.expense_input, 3, 1)

        save_button = QPushButton("Save")
        grid.addWidget(save_button, 4, 0, 1, 2)
        save_button.clicked.connect(self.save_data)

        self.conn = sqlite3.connect('budget.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS budget
            (income REAL, expenses REAL)
        ''')

    def save_data(self):
        try:
            income = float(self.income_input.text())
            expenses = float(self.expense_input.text())

            self.cursor.execute("INSERT INTO budget VALUES (?, ?)", (income, expenses))
            self.conn.commit()

            self.income_input.clear()
            self.expense_input.clear()

            self.display_data()

            # Create a CSV file

            with open('budget.csv', 'a', newline='') as file:

                writer = csv.writer(file)

                writer.writerow([income, expenses])
            
            QMessageBox.information(self, "Success", "Data saved successfully!")
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input. Please enter valid numbers for income and expenses.")
        except Exception as e:
            QMessageBox.critical(self, "Error", "An error occurred: " + str(e))

    def display_data(self):
        self.table_widget.setRowCount(0)
        self.cursor.execute("SELECT * FROM budget")
        rows = self.cursor.fetchall()
        for row in rows:
            self.table_widget.insertRow(self.table_widget.rowCount())
            self.table_widget.setItem(self.table_widget.rowCount() - 1, 0, QTableWidgetItem(str(row[0])))
            self.table_widget.setItem(self.table_widget.rowCount() - 1, 1, QTableWidgetItem(str(row[1])))
