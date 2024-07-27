import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class ExpenseTrackingScreen(tk.Toplevel):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        if 'forest-dark' not in ttk.Style().theme_names():
            self.tk.call('source', 'forest-dark.tcl')
            ttk.Style().theme_use('forest-dark')
        self.title("Expense Tracking")
        self.geometry("800x600")
        self.configure(bg="black")
        self.init_database()
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.back_to_dashboard)

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="20 20 20 20", style='MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        title_label = ttk.Label(mainframe, text="Expense Tracking", font=("Helvetica", 20, "bold"),
                                style='Title.TLabel')
        title_label.grid(column=1, row=0, columnspan=2, pady=20)

        description_label = ttk.Label(mainframe, text="Expense Description", font=("Helvetica", 12),
                                      style='Label.TLabel')
        description_label.grid(column=1, row=1, sticky=tk.W, pady=5)
        self.expense_description = ttk.Entry(mainframe, width=25)
        self.expense_description.grid(column=2, row=1, sticky=(tk.W, tk.E))

        amount_label = ttk.Label(mainframe, text="Expense Amount", font=("Helvetica", 12), style='Label.TLabel')
        amount_label.grid(column=1, row=2, sticky=tk.W, pady=5)
        self.expense_amount = ttk.Entry(mainframe, width=25)
        self.expense_amount.grid(column=2, row=2, sticky=(tk.W, tk.E))

        add_button = ttk.Button(mainframe, text="Add Expense", command=self.add_expense)
        add_button.grid(column=1, row=3, pady=20)

        help_button = ttk.Button(mainframe, text="Help", command=self.show_help)
        help_button.grid(column=2, row=3, pady=20)

        self.expense_list = tk.Listbox(mainframe, width=50, height=15)
        self.expense_list.grid(column=1, row=4, columnspan=2, pady=10)

        back_button = ttk.Button(mainframe, text="Back", command=self.back_to_dashboard)
        back_button.grid(column=1, row=5, columnspan=2, pady=10)

        self.load_expenses()

    def init_database(self):
        self.conn = sqlite3.connect('expenses.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                              (id INTEGER PRIMARY KEY, description TEXT, amount REAL)''')
        self.conn.commit()

    def add_expense(self):
        description = self.expense_description.get()
        amount = self.expense_amount.get()
        if description and amount:
            try:
                amount = float(amount)
                self.cursor.execute("INSERT INTO expenses (description, amount) VALUES (?, ?)", (description, amount))
                self.conn.commit()
                self.expense_list.insert(tk.END, f"{description}: ${amount:.2f}")
                self.expense_description.delete(0, tk.END)
                self.expense_amount.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for the amount.")
        else:
            messagebox.showerror("Error", "Please enter both description and amount.")

    def load_expenses(self):
        self.expense_list.delete(0, tk.END)
        self.cursor.execute("SELECT description, amount FROM expenses")
        for row in self.cursor.fetchall():
            self.expense_list.insert(tk.END, f"{row[0]}: ${row[1]:.2f}")

    def show_help(self):
        help_text = """
        Expense Tracking Help:

        1. Enter the description of your expense in the 'Expense Description' field.
        2. Enter the amount of your expense in the 'Expense Amount' field.
        3. Click 'Add Expense' to save the expense.
        4. Your expenses will be displayed in the list below.
        5. Click 'Back' to return to the dashboard.

        Tips:
        - Be specific in your descriptions to better track your spending.
        - Enter the amount as a number (e.g., 10.50 for $10.50).
        - All expenses are automatically saved to the database.
        """
        messagebox.showinfo("Help", help_text)

    def back_to_dashboard(self):
        if hasattr(self, 'conn'):
            self.conn.close()
        self.main_window.deiconify()  # Show the dashboard
        self.destroy()  # Close the ExpenseTrackingScreen
    def on_closing(self):
        if hasattr(self, 'conn'):
            self.conn.close()
        self.main_window.deiconify()  # Ensure dashboard is shown when closing
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = ExpenseTrackingScreen(root)
    app.mainloop()