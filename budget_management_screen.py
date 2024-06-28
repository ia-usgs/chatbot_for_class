import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import csv
import pandas as pd

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

        ttk.Label(mainframe, text="Budget Management", font=("Helvetica", 16)).grid(column=1, row=1, columnspan=2, sticky=tk.W)

        self.table_widget = ttk.Treeview(mainframe, columns=("Income", "Expenses"), show="headings")
        self.table_widget.heading("Income", text="Income")
        self.table_widget.heading("Expenses", text="Expenses")
        self.table_widget.grid(column=1, row=2, columnspan=2, sticky=(tk.W, tk.E))

        ttk.Label(mainframe, text="Income:").grid(column=1, row=3, sticky=tk.W)
        self.income_input = ttk.Entry(mainframe, width=25)
        self.income_input.grid(column=2, row=3, sticky=(tk.W, tk.E))

        ttk.Label(mainframe, text="Expenses:").grid(column=1, row=4, sticky=tk.W)
        self.expense_input = ttk.Entry(mainframe, width=25)
        self.expense_input.grid(column=2, row=4, sticky=(tk.W, tk.E))

        save_button = ttk.Button(mainframe, text="Save", command=self.save_data)
        save_button.grid(column=1, row=5, columnspan=2, sticky=tk.W)

        self.conn = sqlite3.connect('budget.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS budget (income REAL, expenses REAL)''')
        self.display_data()

    def save_data(self):
        try:
            income = float(self.income_input.get())
            expenses = float(self.expense_input.get())

            self.cursor.execute("INSERT INTO budget VALUES (?, ?)", (income, expenses))
            self.conn.commit()

            self.income_input.delete(0, tk.END)
            self.expense_input.delete(0, tk.END)

            self.display_data()

            with open('budget.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([income, expenses])

            messagebox.showinfo("Success", "Data saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers for income and expenses.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_data(self):
        for row in self.table_widget.get_children():
            self.table_widget.delete(row)
        self.cursor.execute("SELECT * FROM budget")
        for row in self.cursor.fetchall():
            self.table_widget.insert("", "end", values=row)

if __name__ == "__main__":
    app = BudgetManagementScreen()
    app.mainloop()