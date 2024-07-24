import tkinter as tk
from tkinter import ttk, messagebox

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
        self.create_widgets()

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="20 20 20 20", style='MainFrame.TFrame')
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(mainframe, text="Expense Tracking", font=("Helvetica", 20, "bold"), style='Title.TLabel')
        title_label.grid(column=1, row=0, columnspan=2, pady=20)

        # Expense Description
        description_label = ttk.Label(mainframe, text="Expense Description", font=("Helvetica", 12), style='Label.TLabel')
        description_label.grid(column=1, row=1, sticky=tk.W, pady=5)
        self.expense_description = ttk.Entry(mainframe, width=25)
        self.expense_description.grid(column=2, row=1, sticky=(tk.W, tk.E))

        # Expense Amount
        amount_label = ttk.Label(mainframe, text="Expense Amount", font=("Helvetica", 12), style='Label.TLabel')
        amount_label.grid(column=1, row=2, sticky=tk.W, pady=5)
        self.expense_amount = ttk.Entry(mainframe, width=25)
        self.expense_amount.grid(column=2, row=2, sticky=(tk.W, tk.E))

        # Add Expense Button
        add_button = ttk.Button(mainframe, text="Add Expense", command=self.add_expense)
        add_button.grid(column=1, row=3, columnspan=2, pady=20)

        # Listbox to display expenses
        self.expense_list = tk.Listbox(mainframe, width=50, height=15)
        self.expense_list.grid(column=1, row=4, columnspan=2, pady=10)

        # Back Button
        back_button = ttk.Button(mainframe, text="Back", command=self.back_to_dashboard)
        back_button.grid(column=1, row=5, columnspan=2, pady=10)

    def add_expense(self):
        description = self.expense_description.get()
        amount = self.expense_amount.get()

        if description and amount:
            self.expense_list.insert(tk.END, f"{description}: ${amount}")
            self.expense_description.delete(0, tk.END)
            self.expense_amount.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both description and amount.")

    def back_to_dashboard(self):
        from dashboard_screen import DashboardScreen  # Local import to avoid circular dependency
        self.destroy()  # Close the ExpenseTrackingScreen window
        DashboardScreen().mainloop()  # Open the DashboardScreen

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = ExpenseTrackingScreen(root)
    app.mainloop()



