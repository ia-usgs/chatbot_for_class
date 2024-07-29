import os
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import csv
from groq import Groq

class ChatBot(tk.Tk):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.initUI()
        self.client = Groq(api_key="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")
        self.model = "llama3-8b-8192"
        self.messages = []

    def initUI(self):
        self.tk.call('source', 'forest-dark.tcl')
        ttk.Style().theme_use('forest-dark')
        self.title("Financial Advisor Chatbot")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Title and Back Button
        title_frame = ttk.Frame(main_frame)
        title_frame.grid(column=0, row=0, columnspan=3, sticky=(tk.W, tk.E))
        title_frame.columnconfigure(1, weight=1)

        back_button = ttk.Button(title_frame, text="Back to Dashboard", command=self.back_to_dashboard)
        back_button.grid(column=0, row=0, sticky=tk.W)

        title_label = ttk.Label(title_frame, text="Financial Advisor Chatbot", font=("Helvetica", 16))
        title_label.grid(column=1, row=0)

        help_button = ttk.Button(title_frame, text="Help", command=self.show_help)
        help_button.grid(column=2, row=0, sticky=tk.E)

        # Chat Output
        self.output_field = scrolledtext.ScrolledText(main_frame, state="disabled", wrap=tk.WORD, font=("Helvetica", 10))
        self.output_field.grid(column=0, row=1, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input Field
        self.input_field = ttk.Entry(main_frame, font=("Helvetica", 10))
        self.input_field.insert(0, "Type your message here...")
        self.input_field.bind("<FocusIn>", self.clear_placeholder)
        self.input_field.configure(foreground='grey')
        self.input_field.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))

        # Send Button
        send_button = ttk.Button(main_frame, text="Send", command=self.send_message)
        send_button.grid(column=2, row=2, sticky=(tk.E))

        self.input_field.bind("<Return>", self.send_message)

        # Configure weights
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.rowconfigure(1, weight=1)

    def clear_placeholder(self, event):
        if self.input_field.get() == "Type your message here...":
            self.input_field.delete(0, tk.END)
            self.input_field.configure(foreground='black')

    def send_message(self, event=None):
        message = self.input_field.get()
        if message == "Type your message here..." or not message.strip():
            return
        self.input_field.delete(0, tk.END)
        self.output_field.configure(state="normal")
        self.output_field.insert(tk.END, f"You: {message}\n\n", "user")

        response_tag = "response"
        self.output_field.tag_configure(response_tag, foreground="white")

        if message.lower() == "what's my budget":
            self.output_field.insert(tk.END, f"Chatbot: {self.get_budget()}\n\n", response_tag)
        elif message.lower() == "what's my income":
            self.output_field.insert(tk.END, f"Chatbot: {self.get_income()}\n\n", response_tag)
        elif message.lower() == "what's my expenses":
            self.output_field.insert(tk.END, f"Chatbot: {self.get_expenses()}\n\n", response_tag)
        else:
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": f"You are a financial advisor. The user's income is {self.get_income()} and expenses are {self.get_expenses()}. Provide strictly financial advice."},
                        {"role": "user", "content": message}
                    ],
                    model=self.model,
                )
                self.output_field.insert(tk.END, f"Chatbot: {chat_completion.choices[0].message.content}\n\n", response_tag)
            except Exception as e:
                self.output_field.insert(tk.END, f"Chatbot: An error occurred: {e}\n\n", response_tag)

        self.output_field.configure(state="disabled")
        self.output_field.see(tk.END)

    def get_budget(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.DictReader(file)
                total_income = sum(float(row['Income']) for row in reader)
                file.seek(0)
                next(reader)  # Skip header
                total_expenses = sum(float(row['Expenses']) for row in reader)
            budget = total_income - total_expenses
            return f"Your budget is: ${budget:.2f}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def get_income(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.DictReader(file)
                total_income = sum(float(row['Income']) for row in reader)
            return f"Your income is: ${total_income:.2f}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def get_expenses(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.DictReader(file)
                total_expenses = sum(float(row['Expenses']) for row in reader)
            return f"Your expenses are: ${total_expenses:.2f}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def show_help(self):
        help_text = """
        Welcome to the Financial Advisor Chatbot!

        Here are some things you can ask or do:

        1. "What's my budget?" - Get your current budget
        2. "What's my income?" - View your total income
        3. "What's my expenses?" - See your total expenses
        4. Ask for financial advice, such as:
           - "How can I save more money?"
           - "Should I invest in stocks or bonds?"
           - "How do I create a retirement plan?"
           - "What's the best way to pay off debt?"
        5. You can also ask about:
           - Budgeting tips
           - Investment strategies
           - Tax planning
           - Insurance advice

        Remember, this chatbot is designed to provide general financial advice. 
        For personalized financial planning, please consult with a certified financial advisor.
        """
        messagebox.showinfo("Chatbot Help", help_text)

    def back_to_dashboard(self):
        from dashboard_screen import DashboardScreen  # Local import to avoid circular dependency
        self.destroy()  # Close the BudgetManagementScreen window
        DashboardScreen().mainloop()  # Open the DashboardScreen

if __name__ == "__main__":
    app = ChatBot()
    app.mainloop()