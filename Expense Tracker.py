import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expense_data = []

    def get_user_input(self):
        try:
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description: ")
            category = input("Enter the expense category (e.g., food, transportation, entertainment): ")

            expense_entry = {
                "amount": amount,
                "description": description,
                "category": category,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.expense_data.append(expense_entry)
            print("Expense recorded successfully!")

        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")

    def save_to_file(self):
        with open("expense_data.json", "w") as file:
            json.dump(self.expense_data, file)

    def display_summary(self):
        total_expenses = sum(entry["amount"] for entry in self.expense_data)
        print(f"Total expenses: ${total_expenses}")

        # Display category-wise expenditure
        category_expenses = {}
        for entry in self.expense_data:
            category = entry["category"]
            category_expenses[category] = category_expenses.get(category, 0) + entry["amount"]

        print("\nCategory-wise Expenditure:")
        for category, expense in category_expenses.items():
            print(f"{category}: ${expense}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Record Expense")
        print("2. Display Summary")
        print("3. Save and Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            expense_tracker.get_user_input()
        elif choice == "2":
            expense_tracker.display_summary()
        elif choice == "3":
            expense_tracker.save_to_file()
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
