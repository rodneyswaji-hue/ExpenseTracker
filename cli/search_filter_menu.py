from models.expense import Expense

def search_filter_menu():
    while True:
        print("\n=== Search / Filter Menu ===")
        print("1. Search by Description")
        print("2. Filter by Category")
        print("3. Filter by Date Range")
        print("4. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter search text: ")
            results = Expense.search_by_description(text)
            for e in results:
                print(f"{e.id}: {e.description} - ${e.amount}")

        elif choice == "2":
            try:
                cat_id = int(input("Enter category ID: "))
                results = Expense.filter_by_category(cat_id)
                for e in results:
                    print(f"{e.id}: {e.description} - ${e.amount}")
            except ValueError:
                print("Invalid category ID.")

        elif choice == "3":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            results = Expense.filter_by_date_range(start, end)
            for e in results:
                print(f"{e.id}: {e.description} - ${e.amount}")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
