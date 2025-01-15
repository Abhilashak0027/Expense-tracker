# Personal Expense Tracker

# List to store expenses (each expense is a dictionary)
expenses = []

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the category (e.g., food, travel, shopping): ").strip()
        description = input("Enter a brief description (optional): ").strip()
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        
        # Validate date format
        from datetime import datetime
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
            return

        expense = {"amount": amount, "category": category, "description": description, "date": date}
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")

# Function to view all expenses
def view_expenses(expenses_list=None):
    if expenses_list is None:
        expenses_list = expenses
    if expenses_list:
        print("\n--- Expenses List ---")
        for i, expense in enumerate(expenses_list, 1):
            print(f"{i}. {expense['date']} | {expense['amount']} | {expense['category']} | {expense['description']}")
    else:
        print("No expenses recorded.")

# Function to sort expenses by amount
def sort_expenses_by_amount():
    if expenses:
        sorted_expenses = sorted(expenses, key=lambda x: x['amount'])
        view_expenses(sorted_expenses)
    else:
        print("No expenses to sort.")

# Function to filter expenses by category
def filter_expenses_by_category():
    category = input("Enter the category to filter: ").strip().lower()
    filtered_expenses = [expense for expense in expenses if expense['category'].lower() == category]
    if filtered_expenses:
        view_expenses(filtered_expenses)
    else:
        print(f"No expenses found for category: {category}")

# Function to update an expense
def update_expense():
    view_expenses()
    try:
        index = int(input("Enter the index of the expense to update (starting from 1): ")) - 1
        if 0 <= index < len(expenses):
            print(f"Updating expense: {expenses[index]}")
            amount = float(input("Enter the new amount: "))
            category = input("Enter the new category: ").strip()
            description = input("Enter a new description: ").strip()

            # Update the selected expense
            expenses[index] = {"amount": amount, "category": category, "description": description, "date": expenses[index]["date"]}
            print("Expense updated successfully!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Function to calculate total expense
def total_expense():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: {total}")

# Function to set a budget for a category
category_budget = {}
def set_category_budget():
    category = input("Enter category to set budget for: ").strip()
    budget = float(input(f"Enter budget for {category}: "))
    category_budget[category] = budget
    print(f"Budget for {category} set to {budget}.")

# Function to check the budget status
def check_budget():
    if not category_budget:
        print("No budgets set.")
        return
    
    for category, budget in category_budget.items():
        total_spent = sum(expense['amount'] for expense in expenses if expense['category'] == category)
        remaining_budget = budget - total_spent
        print(f"Category: {category}, Total Spent: {total_spent}, Remaining Budget: {remaining_budget}")

# Function to show expense summary
def expense_summary():
    total_expenses_count = len(expenses)
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total_expenses_count}")
    print(f"Total Spent: {total_spent}")

# Function to clear all expenses
def clear_expenses():
    global expenses
    expenses = []
    print("All expenses have been cleared.")

# Menu to interact with the program
def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Sort Expenses by Amount")
        print("4. Filter Expenses by Category")
        print("5. Update Expense")
        print("6. Total Expense")
        print("7. Set Category Budget")
        print("8. Check Category Budget")
        print("9. Expense Summary")
        print("10. Clear All Expenses")
        print("11. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            sort_expenses_by_amount()
        elif choice == "4":
            filter_expenses_by_category()
        elif choice == "5":
            update_expense()
        elif choice == "6":
            total_expense()
        elif choice == "7":
            set_category_budget()
        elif choice == "8":
            check_budget()
        elif choice == "9":
            expense_summary()
        elif choice == "10":
            clear_expenses()
        elif choice == "11":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the main function to start the tracker
if __name__ == "__main__":
    main()
