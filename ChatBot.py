import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
import csv
from groq import Groq

class ChatBot(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.client = Groq(api_key="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")
        self.model = "llama3-8b-8192"
        self.messages = []

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Chatbot')

        layout = QVBoxLayout()

        self.inputField = QLineEdit()
        self.inputField.returnPressed.connect(self.sendMessage)
        layout.addWidget(self.inputField)

        self.outputField = QTextEdit()
        self.outputField.setReadOnly(True)
        layout.addWidget(self.outputField)

        self.setLayout(layout)

        self.show()

    def sendMessage(self):
        message = self.inputField.text()
        self.inputField.clear()
        self.outputField.append(f"You: {message}")
        if message.lower() == "what's my budget":
            self.outputField.append(self.getBudget())
        elif message.lower() == "what's my income":
            self.outputField.append(self.getIncome())
        elif message.lower() == "what's my expenses":
            self.outputField.append(self.getExpenses())
        else:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    # Start with a system message to set the tone
                    {"role": "system", 
                     f"content": f"You are a financial advisor. Information about you to know is: My income is {self.getIncome()} and my expenses are {self.getExpenses()}. Please don't forget that. Also, you are only allowed to talk strictly about financial advise."},
                    # Add the user's question
                    {"role": "user", "content": message}
                ],
                model=self.model,
            )
            self.outputField.append(" ")
            self.outputField.append(f"Chatbot: {chat_completion.choices[0].message.content}")
            self.outputField.append(" ")
        self.outputField.moveCursor(QTextCursor.End)
        
    def getBudget(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.DictReader(file)
                total_income = 0
                total_expenses = 0
                for row in reader:
                    total_income += float(row['Income'])
                    total_expenses += float(row['Expenses'])
                return f"Your budget is: {total_income - total_expenses}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def getIncome(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.reader(file)
                total_income = 0
                for row in reader:
                    total_income += float(row[0])
                return f"Your income is: {total_income:.2f}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def getExpenses(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.reader(file)
                total_expenses = 0
                for row in reader:
                    total_expenses += float(row[1])
                return f"Your expenses are: {total_expenses:.2f}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def closeEvent(self, event):
        event.accept()

    def clearOutput(self):
        self.outputField.clear()

    def clearInput(self):
        self.inputField.clear()

    def clearBoth(self):
        self.clearOutput()
        self.clearInput()