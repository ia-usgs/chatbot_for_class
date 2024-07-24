from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QListWidget, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtGui import QFont
import PyPDF2

class ReportsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Reports")
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet("background-color: black; color: white;")  # Set dark background and white text
        self.createWidgets()

    def createWidgets(self):
        grid = QGridLayout()
        self.setLayout(grid)

        label = QLabel("Reports")
        label.setFont(QFont("Helvetica", 16))
        grid.addWidget(label, 0, 0, 1, 2)  # Span across two columns

        # Input field for report filter
        self.reportFilterInput = QLineEdit(self)
        self.reportFilterInput.setPlaceholderText("Filter reports...")
        self.reportFilterInput.setStyleSheet("background-color: #333; color: white;")  # Dark input field
        grid.addWidget(self.reportFilterInput, 1, 0, 1, 2)  # Span across two columns

        # Button to upload PDF
        uploadButton = QPushButton("Upload PDF", self)
        uploadButton.setStyleSheet("background-color: #555; color: white;")
        uploadButton.clicked.connect(self.uploadPDF)
        grid.addWidget(uploadButton, 2, 0)

        # Button to generate reports
        generateButton = QPushButton("Generate Report", self)
        generateButton.setStyleSheet("background-color: #555; color: white;")
        generateButton.clicked.connect(self.generateReport)
        grid.addWidget(generateButton, 2, 1)

        # Button to refresh reports
        refreshButton = QPushButton("Refresh Reports", self)
        refreshButton.setStyleSheet("background-color: #555; color: white;")
        refreshButton.clicked.connect(self.refreshReports)
        grid.addWidget(refreshButton, 2, 2)

        # List widget to display reports
        self.reportList = QListWidget(self)
        self.reportList.setStyleSheet("background-color: #333; color: white;")  # Dark list widget
        grid.addWidget(self.reportList, 3, 0, 1, 3)  # Span across three columns

        # Load initial reports
        self.loadReports()

    def loadReports(self):
        # Placeholder for loading reports
        self.reportList.clear()
        reports = ["Report 1: Monthly Expenses", "Report 2: Yearly Summary", "Report 3: Category Breakdown"]
        self.reportList.addItems(reports)

    def uploadPDF(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Upload PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if filePath:
            self.readPDF(filePath)

    def readPDF(self, filePath):
        try:
            with open(filePath, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                content = ""
                for page in reader.pages:
                    content += page.extract_text() + "\n"
                self.reportList.addItem(f"PDF Report: {filePath.split('/')[-1]}")
                self.reportList.addItem(content.strip())  # Add the content to the list
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to read PDF: {e}")

    def generateReport(self):
        report_filter = self.reportFilterInput.text()
        if report_filter:
            QMessageBox.information(self, "Report Generated", f"Report with filter '{report_filter}' generated.")
        else:
            QMessageBox.warning(self, "No Filter", "Please enter a filter to generate a report.")

    def refreshReports(self):
        self.loadReports()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = ReportsScreen()
    window.show()
    sys.exit(app.exec_())
