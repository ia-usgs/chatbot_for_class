from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import sys

class SavingsGoalsScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Savings Goals")
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("background-color: #121212; color: #E0E0E0;")  # Dark theme
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        titleLabel = QLabel("Savings Goals")
        titleLabel.setFont(QFont("Helvetica", 20))
        grid.addWidget(titleLabel, 0, 0, 1, 2)  # Span across two columns

        self.goalInput = QLineEdit(self)
        self.goalInput.setPlaceholderText("Enter new savings goal...")
        self.goalInput.setStyleSheet("background-color: #333; color: white;")
        grid.addWidget(self.goalInput, 1, 0, 1, 2)

        addButton = QPushButton("Add Goal", self)
        addButton.setStyleSheet("background-color: #555; color: white;")
        addButton.clicked.connect(self.addGoal)
        grid.addWidget(addButton, 2, 0)

        refreshButton = QPushButton("Refresh Goals", self)
        refreshButton.setStyleSheet("background-color: #555; color: white;")
        refreshButton.clicked.connect(self.refreshGoals)
        grid.addWidget(refreshButton, 2, 1)

        self.goalList = QListWidget(self)
        self.goalList.setStyleSheet("background-color: #333; color: white;")
        grid.addWidget(self.goalList, 3, 0, 1, 2)

        backButton = QPushButton("Back to Dashboard", self)
        backButton.setStyleSheet("background-color: #FF5722; color: white;")
        backButton.clicked.connect(self.backToDashboard)
        grid.addWidget(backButton, 4, 0, 1, 2)

        self.loadGoals()

    def loadGoals(self):
        self.goalList.clear()
        goals = ["Goal 1: Save for Vacation", "Goal 2: Emergency Fund", "Goal 3: New Laptop"]
        self.goalList.addItems(goals)

    def addGoal(self):
        new_goal = self.goalInput.text()
        if new_goal:
            self.goalList.addItem(new_goal)
            self.goalInput.clear()
            QMessageBox.information(self, "Goal Added", f"Savings goal '{new_goal}' added.")
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a savings goal.")

    def refreshGoals(self):
        self.loadGoals()

    def backToDashboard(self):
        self.close()  # Close current window or implement logic to return to the dashboard

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SavingsGoalsScreen()
    window.show()
    sys.exit(app.exec_())
