from cli.category_menu import category_menu
from cli.expense_menu import expense_menu
from cli.reporting_menu import reporting_menu
from cli.search_filter_menu import search_filter_menu

def main_menu():
    while True:
        print("\n=== Expense Tracker Main Menu ===")
        print("1. Manage Categories")
        print("2. Manage Expenses")
        print("3. Reporting")
        print("4. Search / Filter")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category_menu()
        elif choice == "2":
            expense_menu()
        elif choice == "3":
            reporting_menu()
        elif choice == "4":
            search_filter_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
