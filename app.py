from main import ChatbotGUI
from dashboard_screen import DashboardScreen

def show_login():
    login_screen = ChatbotGUI()
    login_screen.mainloop()

def show_dashboard():
    dashboard_screen = DashboardScreen()
    dashboard_screen.mainloop()

if __name__ == "__main__":
    show_login()