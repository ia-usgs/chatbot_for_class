import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import csv
from groq import Groq


class ChatBot(tk.Tk):
    def __init__(self):
        """
        Initializes the ChatBot GUI window.
        """
        # Call the constructor of the parent class
        super().__init__()
        
        # Load the Forest-Dark theme using the Tkinter call method
        self.tk.call('source', 'forest-dark.tcl')
        
        # Use the Forest-Dark theme for the GUI
        ttk.Style().theme_use('forest-dark')
        
        # Set the title of the GUI window to "Chatbot"
        self.title("Chatbot")
        
        # Set the size of the GUI window to 800x600 pixels
        self.geometry("800x600")
        
        # Create the widgets for the GUI
        self.create_widgets()
        
        # Create a Groq client with the OpenAI API key
        self.client = Groq(api_key="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")
        
        # Set the model to use for the Groq client
        self.model = "llama3-8b-8192"
        
        # Initialize an empty list to store the messages
        self.messages = []

    def create_widgets(self):
        # Create an Entry widget for the user to input messages
        self.input_field = ttk.Entry(self)
        self.input_field.insert(0, "Type your message here...")
        self.input_field.bind("<FocusIn>", lambda event: self.input_field.delete(0, tk.END) if self.input_field.get() == "Type your message here..." else None)
        self.input_field.configure(foreground='grey')
        self.input_field.grid(column=0, row=0, columnspan=3, sticky=(tk.W, tk.E))

        # Create a "send" button for sending messages
        send_button = ttk.Button(self, text="Send", command=self.send_message)
        send_button.grid(column=2, row=0, sticky=(tk.E))

        # Bind the Enter key to the send_message method for sending messages
        self.input_field.bind("<Return>", self.send_message)

        # Create a ScrolledText widget for displaying messages
        self.output_field = scrolledtext.ScrolledText(self, state="disabled")
        self.output_field.grid(column=0, row=1, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        # Set the column weights to make the chatbot's response field expand horizontally
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        # Set the row weight to make the chatbot's response field expand vertically
        self.rowconfigure(1, weight=1)

    def send_message(self, event=None):
        # Get the message input by the user
        message = self.input_field.get()
        # Clear the input field
        self.input_field.delete(0, tk.END)
        # Enable editing in the output field
        self.output_field.configure(state="normal")
        # Insert the user's message into the output field
        self.output_field.insert(tk.END, "You: ", "user")
        self.output_field.insert(tk.END, f"{message}\n\n")
        
        response_tag = "response"  # Define a tag for the chatbot's responses
        # Configure the response tag with a white text color
        self.output_field.tag_configure(response_tag, foreground="white")
        
        # Check if the user's message is asking for their budget
        if message.lower() == "what's my budget":
            # Insert the chatbot's response into the output field
            self.output_field.insert(tk.END, "Chatbot: ", response_tag)
            self.output_field.insert(tk.END, f"{self.get_budget()}\n", response_tag)
        # Check if the user's message is asking for their income
        elif message.lower() == "what's my income":
            self.output_field.insert(tk.END, "Chatbot: ", response_tag)
            self.output_field.insert(tk.END, f"{self.get_income()}\n", response_tag)
        # Check if the user's message is asking for their expenses
        elif message.lower() == "what's my expenses":
            self.output_field.insert(tk.END, "Chatbot: ", response_tag)
            self.output_field.insert(tk.END, f"{self.get_expenses()}\n", response_tag)
        else:
            # Send the user's message to the chatbot and get the response
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"You are a financial advisor. Information about you to know is: My income is {self.get_income()} and my expenses are {self.get_expenses()}. Please don't forget that. Also, you are only allowed to talk strictly about financial advice."},
                    {"role": "user", "content": message}
                ],
                model=self.model,
            )
            # Insert the chatbot's response into the output field
            self.output_field.insert(tk.END, "Chatbot: ", response_tag)
            self.output_field.insert(tk.END, f"{chat_completion.choices[0].message.content}\n\n", response_tag)  # Add newline for spacing
        
        # Disable editing in the output field
        self.output_field.configure(state="disabled")
        # Scroll the output field to the end
        self.output_field.yview(tk.END)

    def get_budget(self):
        try:
            # Open the budget.csv file in read mode
            with open('budget.csv', 'r') as file:
                # Create a DictReader object to read the CSV file
                reader = csv.DictReader(file)
                # Initialize variables to store the total income and total expenses
                total_income = 0
                total_expenses = 0
                # Iterate over each row in the CSV file
                for row in reader:
                    # Convert the 'Income' column value to a float and add it to the total income
                    total_income += float(row['Income'])
                    # Convert the 'Expenses' column value to a float and add it to the total expenses
                    total_expenses += float(row['Expenses'])
                # Calculate the budget by subtracting the total expenses from the total income
                budget = total_income - total_expenses
                return f"Your budget is: {budget}"
        except FileNotFoundError:
            # Return an error message if the budget.csv file is not found
            return "Error: budget.csv not found"
        except Exception as e:
            # Return an error message if any other exception occurs
            return f"Error: {e}"

    def get_income(self):
        """
        Calculate and return the total income from the budget.csv file.
        """
        try:
            # Open the budget.csv file in read mode
            with open('budget.csv', 'r') as file:
                # Create a CSV reader object to read the file
                reader = csv.reader(file)
                # Initialize a variable to store the total income
                total_income = 0
                # Iterate over each row in the CSV file
                for row in reader:
                    # Get the first column value (income) from the row and convert it to a float
                    # Add it to the total income
                    total_income += float(row[0])
                # Format the total income with 2 decimal places and return it
                return f"Your income is: {total_income:.2f}"
        except FileNotFoundError:
            # Return an error message if the budget.csv file is not found
            return "Error: budget.csv not found"
        except Exception as e:
            # Return an error message if any other exception occurs
            return f"Error: {e}"

    def get_expenses(self):
        """
        Calculate and return the total expenses from the budget.csv file.
        """
        try:
            # Open the budget.csv file in read mode
            with open('budget.csv', 'r') as file:
                # Create a CSV reader object to read the file
                reader = csv.reader(file)
                # Initialize a variable to store the total expenses
                total_expenses = 0
                # Iterate over each row in the CSV file
                for row in reader:
                    # Get the second column value (expenses) from the row and convert it to a float
                    # Add it to the total expenses
                    total_expenses += float(row[1])
                # Format the total expenses with 2 decimal places and return it
                return f"Your expenses are: {total_expenses:.2f}"
        except FileNotFoundError:
            # Return an error message if the budget.csv file is not found
            return "Error: budget.csv not found"
        except Exception as e:
            # Return an error message if any other exception occurs
            return f"Error: {e}"

if __name__ == "__main__":
    app = ChatBot()
    app.mainloop()