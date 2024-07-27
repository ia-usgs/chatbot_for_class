from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMessageBox, \
    QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import csv
import os
import sqlite3


class ReportsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

    def initUI(self):
        self.setWindowTitle("Financial Reports")
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("background-color: #2b2b2b; color: white;")
        self.createWidgets()

    def initDB(self):
        # Initialize income database
        self.income_conn = sqlite3.connect('income.db')
        self.income_cursor = self.income_conn.cursor()
        self.income_cursor.execute('''CREATE TABLE IF NOT EXISTS income
                                      (id INTEGER PRIMARY KEY, amount REAL)''')

        # Initialize expenses database
        self.expenses_conn = sqlite3.connect('expenses.db')
        self.expenses_cursor = self.expenses_conn.cursor()
        self.expenses_cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                                        (id INTEGER PRIMARY KEY, amount REAL)''')

    def createWidgets(self):
        layout = QVBoxLayout()

        # Top bar with title, help, and back buttons
        top_bar = QHBoxLayout()
        title = QLabel("Financial Reports")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        top_bar.addWidget(title)
        top_bar.addStretch(1)

        help_button = self.createButton("Help", self.showHelp)
        back_button = self.createButton("Back", self.backToDashboard)
        top_bar.addWidget(help_button)
        top_bar.addWidget(back_button)
        layout.addLayout(top_bar)

        # CSV upload and report generation section
        action_layout = QHBoxLayout()
        self.reportFilterInput = QLineEdit()
        self.reportFilterInput.setPlaceholderText("Enter report filter...")
        self.reportFilterInput.setStyleSheet("background-color: #3a3a3a; color: white; padding: 5px;")
        action_layout.addWidget(self.reportFilterInput)

        upload_button = self.createButton("Upload CSV", self.uploadCSV)
        generate_button = self.createButton("Generate Report", self.generateReport)
        refresh_button = self.createButton("Refresh", self.refreshReports)

        action_layout.addWidget(upload_button)
        action_layout.addWidget(generate_button)
        action_layout.addWidget(refresh_button)
        layout.addLayout(action_layout)

        # Report list
        self.reportList = QListWidget()
        self.reportList.setStyleSheet("background-color: #3a3a3a; color: white;")
        layout.addWidget(self.reportList)

        self.setLayout(layout)
        self.loadReports()

    def createButton(self, text, callback):
        button = QPushButton(text)
        button.setStyleSheet("""
            QPushButton {
                background-color: #4a4a4a;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
            }
        """)
        button.clicked.connect(callback)
        return button

    def loadReports(self):
        self.reportList.clear()
        self.reportList.addItem("Available Reports:")
        self.reportList.addItem("1. Monthly Expenses Summary")
        self.reportList.addItem("2. Yearly Income Overview")
        self.reportList.addItem("3. Budget vs. Actual Spending")
        self.reportList.addItem("4. Savings Goal Progress")

    def uploadCSV(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Upload CSV", "", "CSV Files (*.csv);;All Files (*)",
                                                  options=options)
        if filePath:
            self.readCSV(filePath)

    def readCSV(self, filePath):
        try:
            with open(filePath, 'r', newline='') as file:
                reader = csv.DictReader(file)
                income_entries = []
                expense_entries = []
                for row in reader:
                    amount = float(row['Amount'])
                    if amount > 0:
                        income_entries.append(amount)
                    else:
                        expense_entries.append(abs(amount))

            self.processCSVContent(income_entries, expense_entries)
            self.reportList.addItem(f"Imported: {os.path.basename(filePath)}")
            QMessageBox.information(self, "Success", "CSV file imported successfully!")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to read CSV: {e}")

    def processCSVContent(self, income_entries, expense_entries):
        self.writeToCSVAndDB('income.csv', income_entries, self.income_cursor, self.income_conn, 'income')
        self.writeToCSVAndDB('expenses.csv', expense_entries, self.expenses_cursor, self.expenses_conn, 'expenses')
        self.displayData(income_entries, expense_entries)

    def writeToCSVAndDB(self, filename, entries, cursor, conn, table):
        try:
            # Write to CSV
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Amount'])
                for amount in entries:
                    writer.writerow([amount])

            # Write to database
            for amount in entries:
                cursor.execute(f"INSERT INTO {table} (amount) VALUES (?)", (amount,))
            conn.commit()
        except Exception as e:
            QMessageBox.warning(self, "File Error", f"Failed to write to {filename}: {e}")

    def displayData(self, income_entries, expense_entries):
        self.reportList.addItem("\nIncome Summary:")
        total_income = sum(income_entries)
        self.reportList.addItem(f"Total Income: ${total_income:.2f}")

        self.reportList.addItem("\nExpense Summary:")
        total_expenses = sum(expense_entries)
        self.reportList.addItem(f"Total Expenses: ${total_expenses:.2f}")

        balance = total_income - total_expenses
        self.reportList.addItem(f"\nCurrent Balance: ${balance:.2f}")

    def generateReport(self):
        report_filter = self.reportFilterInput.text()
        if report_filter:
            self.reportList.addItem(f"\nGenerated Report: {report_filter}")

            # Read from databases and generate report
            income_data = self.income_cursor.execute("SELECT * FROM income").fetchall()
            expense_data = self.expenses_cursor.execute("SELECT * FROM expenses").fetchall()

            self.reportList.addItem("Income Data:")
            for row in income_data:
                self.reportList.addItem(f"ID: {row[0]}, Amount: ${row[1]:.2f}")

            self.reportList.addItem("\nExpense Data:")
            for row in expense_data:
                self.reportList.addItem(f"ID: {row[0]}, Amount: ${row[1]:.2f}")

            QMessageBox.information(self, "Report Generated", f"Report '{report_filter}' has been generated.")
        else:
            QMessageBox.warning(self, "No Filter", "Please enter a filter to generate a report.")

    def refreshReports(self):
        self.loadReports()
        QMessageBox.information(self, "Refreshed", "Reports have been refreshed.")

    def showHelp(self):
        help_message = (
            "Financial Reports Help:\n\n"
            "1. Upload CSV: Import your financial data.\n"
            "2. Generate Report: Create a report using the filter.\n"
            "3. Refresh: Reload the initial report list.\n"
            "4. Back: Return to the main dashboard.\n\n"
            "For assistance, contact support@financialapp.com"
        )
        QMessageBox.information(self, "Help", help_message)

    def backToDashboard(self):
        self.close()

    def closeEvent(self, event):
        # Close database connections when the window is closed
        self.income_conn.close()
        self.expenses_conn.close()
        super().closeEvent(event)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = ReportsScreen()
    window.show()
    sys.exit(app.exec_())