import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Set up main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("300x200")

# Input fields
tk.Label(root, text="Amount").grid(row=0, column=0)
tk.Label(root, text="Category").grid(row=1, column=0)
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0)

amount_entry = tk.Entry(root)
category_entry = tk.Entry(root)
date_entry = tk.Entry(root)

amount_entry.grid(row=0, column=1)
category_entry.grid(row=1, column=1)
date_entry.grid(row=2, column=1)

# In-memory storage for expenses
expenses = []

# Add expense to in-memory list
def add_expense():
    amount, category, date = amount_entry.get(), category_entry.get(), date_entry.get()
    if amount and category and date:
        expenses.append({"amount": float(amount), "category": category, "date": date})
        messagebox.showinfo("Success", "Expense added!")
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Show expense pie chart
def view_expenses():
    if not expenses:
        messagebox.showwarning("No Data", "No expenses recorded yet.")
        return

    # Calculate total by category
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]

    categories, amounts = list(category_totals.keys()), list(category_totals.values())

    # Create a pie chart
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Distribution")
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.show()

# Buttons
tk.Button(root, text="Add Expense", command=add_expense).grid(row=3, column=0)
tk.Button(root, text="View Expenses", command=view_expenses).grid(row=3, column=1)

# Run the application
root.mainloop()
