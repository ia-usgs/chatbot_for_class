from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import sys
import sqlite3

class SavingsGoalsScreen(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.initDB()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Savings Goals")
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("background-color: #121212; color: #E0E0E0;")  # Dark theme
        self.createWidgets()

    def initDB(self):
        self.conn = sqlite3.connect('savings.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS savings_goals
                              (id INTEGER PRIMARY KEY, goal TEXT)''')
        self.conn.commit()

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

        refreshButton = QPushButton("Delete All Goals", self)
        refreshButton.setStyleSheet("background-color: #555; color: white;")
        refreshButton.clicked.connect(self.deleteAllGoals)
        grid.addWidget(refreshButton, 2, 1)

        deleteButton = QPushButton("Delete Selected Goal", self)
        deleteButton.setStyleSheet("background-color: #555; color: white;")
        deleteButton.clicked.connect(self.deleteSelectedGoal)
        grid.addWidget(deleteButton, 2, 2)

        self.goalList = QListWidget(self)
        self.goalList.setStyleSheet("background-color: #333; color: white;")
        grid.addWidget(self.goalList, 3, 0, 1, 3)

        backButton = QPushButton("Back to Dashboard", self)
        backButton.setStyleSheet("background-color: #FF5722; color: white;")
        backButton.clicked.connect(self.backToDashboard)
        grid.addWidget(backButton, 4, 0, 1, 3)

        self.loadGoals()

    def loadGoals(self):
        self.goalList.clear()
        self.cursor.execute("SELECT * FROM savings_goals")
        goals = self.cursor.fetchall()
        for goal in goals:
            self.goalList.addItem(f"Goal {goal[0]}: {goal[1]}")

    def addGoal(self):
        new_goal = self.goalInput.text()
        if new_goal:
            self.cursor.execute("INSERT INTO savings_goals (goal) VALUES (?)", (new_goal,))
            self.conn.commit()
            self.goalInput.clear()
            self.loadGoals()
            print("Goal added: " + new_goal)
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a savings goal.")

    def deleteAllGoals(self):
        self.cursor.execute("DELETE FROM savings_goals")
        self.conn.commit()
        self.loadGoals()
        print("All goals deleted")

    def deleteSelectedGoal(self):
        selected_item = self.goalList.currentItem()
        if selected_item:
            goal_id = int(selected_item.text().split(":")[0].split(" ")[1])
            self.cursor.execute("DELETE FROM savings_goals WHERE id = ?", (goal_id,))
            self.conn.commit()
            self.loadGoals()
            print(f"Goal {goal_id} deleted")
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a goal to delete.")

    def backToDashboard(self):
        self.close()

    def closeEvent(self, event):
        self.conn.close()
        event.accept()
        QApplication.quit()  # This will end the Qt event loop

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SavingsGoalsScreen()
    window.show()
    sys.exit(app.exec_())