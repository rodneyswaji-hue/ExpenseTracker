from models.expense import Expense

def expense_menu():
    while True:
        print("\n=== Expense Menu ===")
        print("1. Create Expense")
        print("2. Delete Expense")
        print("3. View All Expenses")
        print("4. Find Expense by ID")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category_id = int(input("Enter category ID: "))
                date = input("Enter date (YYYY-MM-DD): ")

                Expense.create(amount, description, category_id, date)
                print("Expense created successfully.")

            except ValueError:
                print("Invalid input. Please check numbers and format.")

        elif choice == "2":
            try:
                exp_id = int(input("Enter expense ID to delete: "))
                Expense.delete(exp_id)
                print("Expense deleted.")
            except ValueError:
                print("ID must be a number.")

        elif choice == "3":
            expenses = Expense.get_all()
            for e in expenses:
                print(f"{e.id}: {e.description} - ${e.amount} (Category {e.category_id}) on {e.date}")

        elif choice == "4":
            try:
                exp_id = int(input("Enter ID: "))
                expense = Expense.find_by_id(exp_id)
                if expense:
                    print(f"{expense.id}: {expense.description} - ${expense.amount} on {expense.date}")
                else:
                    print("Expense not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
