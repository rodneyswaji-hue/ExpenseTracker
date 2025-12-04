from models.expense import Expense

def reporting_menu():
    while True:
        print("\n=== Reporting Menu ===")
        print("1. Total Spending")
        print("2. Spending by Category")
        print("3. Monthly Spending")
        print("4. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            total = Expense.total_spending()
            print(f"Total spending: ${total}")

        elif choice == "2":
            results = Expense.spending_by_category()
            for name, amount in results:
                print(f"{name}: ${amount}")

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            total = Expense.monthly_spending(month)
            print(f"Total spending for {month}: ${total}")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
