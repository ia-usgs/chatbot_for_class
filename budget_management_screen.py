import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class BudgetManagementScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Budget Management")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="Budget Management", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=5, sticky=tk.W)

        self.table_widget = ttk.Treeview(mainframe, columns=("Income", "Expenses"), show="headings")
        self.table_widget.heading("Income", text="Income")
        self.table_widget.heading("Expenses", text="Expenses")
        self.table_widget.grid(column=0, row=1, columnspan=5, sticky=(tk.W, tk.E))

        ttk.Label(mainframe, text="Income:").grid(column=0, row=2, sticky=tk.W)
        self.income_input = ttk.Entry(mainframe, width=25)
        self.income_input.grid(column=1, row=2, sticky=(tk.W, tk.E))

        ttk.Label(mainframe, text="Expenses:").grid(column=2, row=2, sticky=tk.W)
        self.expense_input = ttk.Entry(mainframe, width=25)
        self.expense_input.grid(column=3, row=2, sticky=(tk.W, tk.E))

        button_frame = ttk.Frame(mainframe)
        button_frame.grid(column=0, row=3, columnspan=5, sticky=(tk.W, tk.E))

        save_button = ttk.Button(button_frame, text="Save", command=self.save_data)
        save_button.grid(column=0, row=0, padx=5, pady=5)

        delete_button = ttk.Button(button_frame, text="Delete Selected", command=self.delete_selected)
        delete_button.grid(column=1, row=0, padx=5, pady=5)

        delete_all_button = ttk.Button(button_frame, text="Delete All", command=self.delete_all)
        delete_all_button.grid(column=2, row=0, padx=5, pady=5)

        help_button = ttk.Button(button_frame, text="Help", command=self.show_help)
        help_button.grid(column=3, row=0, padx=5, pady=5)

        back_button = ttk.Button(button_frame, text="Back", command=self.back_to_dashboard)
        back_button.grid(column=4, row=0, padx=5, pady=5)

        self.budget_summary_label = ttk.Label(mainframe, text="", font=("Helvetica", 12))
        self.budget_summary_label.grid(column=0, row=4, columnspan=5, sticky=tk.W)

        self.income_conn = sqlite3.connect('income.db')
        self.income_cursor = self.income_conn.cursor()
        self.income_cursor.execute('''CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY, amount REAL)''')

        self.expense_conn = sqlite3.connect('expenses.db')
        self.expense_cursor = self.expense_conn.cursor()
        self.expense_cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, amount REAL)''')

        self.display_data()

    def save_data(self):
        try:
            income = float(self.income_input.get())
            expenses = float(self.expense_input.get())

            with open('budget.csv', 'a', newline='') as budget_file:
                writer = csv.writer(budget_file)
                writer.writerow([income, expenses])

            self.income_cursor.execute("INSERT INTO income (amount) VALUES (?)", (income,))
            self.income_conn.commit()

            self.expense_cursor.execute("INSERT INTO expenses (amount) VALUES (?)", (expenses,))
            self.expense_conn.commit()

            self.income_input.delete(0, tk.END)
            self.expense_input.delete(0, tk.END)
            self.display_data()

            print("Success", "Data saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers for income and expenses.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")

    def get_financial_advice(self, income, expenses):
        if expenses > income:
            return self.budget_summary_label.config(
                text=f"You're spending more than you earn. Consider cutting back on expenses.")
        elif expenses < income * 0.5:
            return self.budget_summary_label.config(
                text=f"Great job! You're saving a good portion of your income.")
        return self.budget_summary_label.config(
            text=f"You're managing your budget well.")

    def display_data(self):
        for row in self.table_widget.get_children():
            self.table_widget.delete(row)

        self.income_cursor.execute("SELECT amount FROM income")
        incomes = self.income_cursor.fetchall()

        self.expense_cursor.execute("SELECT amount FROM expenses")
        expenses = self.expense_cursor.fetchall()

        for income, expense in zip(incomes, expenses):
            self.table_widget.insert("", "end", values=(income[0], expense[0]))

        if self.table_widget.get_children():
            print(f"Displayed {len(self.table_widget.get_children())} rows.")
        else:
            print("No valid data found in the income and expenses tables.")

    def delete_selected(self):
        selected_item = self.table_widget.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a row to delete.")
            return
        item = self.table_widget.item(selected_item)
        income, expenses = item['values']
        self.income_cursor.execute("DELETE FROM income WHERE amount = ?", (income,))
        self.income_conn.commit()
        self.expense_cursor.execute("DELETE FROM expenses WHERE amount = ?", (expenses,))
        self.expense_conn.commit()
        self.display_data()
        print("Success", "Selected row deleted successfully!")

    def delete_all(self):
        self.income_cursor.execute("DELETE FROM income")
        self.income_conn.commit()
        self.expense_cursor.execute("DELETE FROM expenses")
        self.expense_conn.commit()
        self.display_data()
        print("Success", "All rows deleted successfully!")

    def back_to_dashboard(self):
        from dashboard_screen import DashboardScreen  # Local import to avoid circular dependency
        self.destroy()  # Close the BudgetManagementScreen window
        DashboardScreen().mainloop()  # Open the DashboardScreen

    def show_help(self):
        help_message = (
            "Budget Management Help:\n\n"
            "1. Enter your monthly income in the 'Income' field.\n"
            "2. Enter your expenses for the week in the 'Expenses' field.\n"
            "3. Click 'Save' to save the data.\n"
            "4. To delete a specific entry, select it from the table and click 'Delete Selected'.\n"
            "5. To delete all entries, click 'Delete All'.\n"
            "6. Click 'Back' to return to the dashboard.\n"
            "7. The summary of your total income and expenses is displayed at the bottom."
        )
        messagebox.showinfo("Help", help_message)

if __name__ == "__main__":
    app = BudgetManagementScreen()
    app.mainloop()