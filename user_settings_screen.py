from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal
import sys

class UserSettingsScreen(QWidget):
    closed = pyqtSignal()  # Signal to emit when the window is closed
    def __init__(self, dashboard):
        super().__init__()
        self.dashboard = dashboard
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Settings")
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("background-color: #121212; color: #E0E0E0;")
        self.createWidgets()

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    def createWidgets(self):
        grid = QGridLayout()
        grid.setAlignment(Qt.AlignTop)
        self.setLayout(grid)

        titleLabel = QLabel("User Settings")
        titleLabel.setFont(QFont("Helvetica", 24))
        titleLabel.setAlignment(Qt.AlignCenter)
        grid.addWidget(titleLabel, 0, 0, 1, 2)

        grid.addWidget(QLabel("First Name:"), 1, 0)
        self.firstNameInput = QLineEdit(self)
        self.firstNameInput.setPlaceholderText("Enter your first name...")
        self.firstNameInput.setStyleSheet("background-color: #FFF; color: #333; padding: 10px;")
        grid.addWidget(self.firstNameInput, 1, 1)

        grid.addWidget(QLabel("Last Name:"), 2, 0)
        self.lastNameInput = QLineEdit(self)
        self.lastNameInput.setPlaceholderText("Enter your last name...")
        self.lastNameInput.setStyleSheet("background-color: #FFF; color: #333; padding: 10px;")
        grid.addWidget(self.lastNameInput, 2, 1)

        grid.addWidget(QLabel("Email:"), 3, 0)
        self.emailInput = QLineEdit(self)
        self.emailInput.setPlaceholderText("Enter your email...")
        self.emailInput.setStyleSheet("background-color: #FFF; color: #333; padding: 10px;")
        grid.addWidget(self.emailInput, 3, 1)

        grid.addWidget(QLabel("Monthly Take-home Pay:"), 4, 0)
        self.salaryInput = QLineEdit(self)
        self.salaryInput.setPlaceholderText("Enter your salary...")
        self.salaryInput.setStyleSheet("background-color: #FFF; color: #333; padding: 10px;")
        grid.addWidget(self.salaryInput, 4, 1)

        saveButton = QPushButton("Save Information", self)
        saveButton.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        saveButton.clicked.connect(self.saveSettings)
        grid.addWidget(saveButton, 5, 0, 1, 2)

        resetButton = QPushButton("Reset Settings", self)
        resetButton.setStyleSheet("background-color: #FF9800; color: white; padding: 10px;")
        resetButton.clicked.connect(self.resetSettings)
        grid.addWidget(resetButton, 6, 0, 1, 2)

        backButton = QPushButton("Back to Dashboard", self)
        backButton.setStyleSheet("background-color: #F44336; color: white; padding: 10px;")
        backButton.clicked.connect(self.backToDashboard)
        grid.addWidget(backButton, 7, 0, 1, 2)

    def saveSettings(self):
        first_name = self.firstNameInput.text()
        last_name = self.lastNameInput.text()
        email = self.emailInput.text()
        salary = self.salaryInput.text()

        if first_name and last_name and email and salary:
            QMessageBox.information(self, "Settings Saved", f"Settings saved for user: {first_name} {last_name}.")
        else:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")

    def resetSettings(self):
        self.firstNameInput.clear()
        self.lastNameInput.clear()
        self.emailInput.clear()
        self.salaryInput.clear()
        QMessageBox.information(self, "Settings Reset", "User settings have been reset.")

    def backToDashboard(self):
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserSettingsScreen()
    window.show()
    sys.exit(app.exec_())
