import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import csv
from groq import Groq
import sv_ttk

class ChatBot(tk.Tk):
    def __init__(self):
        super().__init__()
        sv_ttk.set_theme("dark")
        self.title("Chatbot")
        self.geometry("300x400")
        self.create_widgets()

        self.client = Groq(api_key="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")
        self.model = "llama3-8b-8192"
        self.messages = []

    def create_widgets(self):
        self.input_field = ttk.Entry(self)
        self.input_field.grid(column=0, row=0, sticky=(tk.W, tk.E))
        self.input_field.bind("<Return>", self.send_message)

        self.output_field = scrolledtext.ScrolledText(self, state="disabled")
        self.output_field.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def send_message(self, event=None):
        message = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.output_field.configure(state="normal")
        self.output_field.insert(tk.END, f"You: {message}\n")
        if message.lower() == "what's my budget":
            self.output_field.insert(tk.END, f"Chatbot: {self.get_budget()}\n")
        elif message.lower() == "what's my income":
            self.output_field.insert(tk.END, f"Chatbot: {self.get_income()}\n")
        elif message.lower() == "what's my expenses":
            self.output_field.insert(tk.END, f"Chatbot: {self.get_expenses()}\n")
        else:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"You are a financial advisor. Information about you to know is: My income is {self.get_income()} and my expenses are {self.get_expenses()}. Please don't forget that. Also, you are only allowed to talk strictly about financial advice."},
                    {"role": "user", "content": message}
                ],
                model=self.model,
            )
            self.output_field.insert(tk.END, f"Chatbot: {chat_completion.choices[0].message.content}\n")
        self.output_field.configure(state="disabled")
        self.output_field.yview(tk.END)

    def get_budget(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.DictReader(file)
                total_income = 0
                total_expenses = 0
                for row in reader:
                    total_income += float(row['Income'])
                    total_expenses += float(row['Expenses'])
                return f"Your budget is: {total_income - total_expenses}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def get_income(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.reader(file)
                total_income = 0
                for row in reader:
                    total_income += float(row[0])
                return f"Your income is: {total_income:.2f}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

    def get_expenses(self):
        try:
            with open('budget.csv', 'r') as file:
                reader = csv.reader(file)
                total_expenses = 0
                for row in reader:
                    total_expenses += float(row[1])
                return f"Your expenses are: {total_expenses:.2f}"
        except FileNotFoundError:
            return "Error: budget.csv not found"
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    app = ChatBot()
    app.mainloop()