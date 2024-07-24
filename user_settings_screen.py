from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QApplication
from PyQt5.QtGui import QFont
import sys

class UserSettingsScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Settings")
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("background-color: #121212; color: #E0E0E0;")
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        titleLabel = QLabel("User Settings")
        titleLabel.setFont(QFont("Helvetica", 20))
        grid.addWidget(titleLabel, 0, 0, 1, 2)

        grid.addWidget(QLabel("Username:"), 1, 0)
        self.usernameInput = QLineEdit(self)
        self.usernameInput.setPlaceholderText("Enter your username...")
        self.usernameInput.setStyleSheet("background-color: #333; color: white;")
        grid.addWidget(self.usernameInput, 1, 1)

        grid.addWidget(QLabel("Email:"), 2, 0)
        self.emailInput = QLineEdit(self)
        self.emailInput.setPlaceholderText("Enter your email...")
        self.emailInput.setStyleSheet("background-color: #333; color: white;")
        grid.addWidget(self.emailInput, 2, 1)

        grid.addWidget(QLabel("Password:"), 3, 0)
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setPlaceholderText("Enter your password...")
        self.passwordInput.setStyleSheet("background-color: #333; color: white;")
        self.passwordInput.setEchoMode(QLineEdit.Password)
        grid.addWidget(self.passwordInput, 3, 1)

        saveButton = QPushButton("Save Settings", self)
        saveButton.setStyleSheet("background-color: #555; color: white;")
        saveButton.clicked.connect(self.saveSettings)
        grid.addWidget(saveButton, 4, 0)

        resetButton = QPushButton("Reset Settings", self)
        resetButton.setStyleSheet("background-color: #555; color: white;")
        resetButton.clicked.connect(self.resetSettings)
        grid.addWidget(resetButton, 4, 1)

        backButton = QPushButton("Back to Dashboard", self)
        backButton.setStyleSheet("background-color: #FF5722; color: white;")
        backButton.clicked.connect(self.backToDashboard)
        grid.addWidget(backButton, 5, 0, 1, 2)

    def saveSettings(self):
        username = self.usernameInput.text()
        email = self.emailInput.text()
        password = self.passwordInput.text()

        if username and email and password:
            QMessageBox.information(self, "Settings Saved", f"Settings saved for user: {username}.")
        else:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")

    def resetSettings(self):
        self.usernameInput.clear()
        self.emailInput.clear()
        self.passwordInput.clear()
        QMessageBox.information(self, "Settings Reset", "User settings have been reset.")

    def backToDashboard(self):
        from dashboard_screen import DashboardScreen  # Local import to avoid circular dependency
        self.destroy()  # Close the ExpenseTrackingScreen window
        DashboardScreen().mainloop()  # Open the DashboardScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserSettingsScreen()
    window.show()
    sys.exit(app.exec_())
