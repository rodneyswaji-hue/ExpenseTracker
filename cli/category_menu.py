from models.category import Category

def category_menu():
    while True:
        print("\n=== Category Menu ===")
        print("1. Create Category")
        print("2. Delete Category")
        print("3. View All Categories")
        print("4. Find Category by ID")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter category name: ")
            Category.create(name)
            print("Category created successfully.")

        elif choice == "2":
            try:
                cat_id = int(input("Enter category ID to delete: "))
                Category.delete(cat_id)
                print("Category deleted.")
            except ValueError:
                print("Invalid input. ID must be a number.")

        elif choice == "3":
            categories = Category.get_all()
            for c in categories:
                print(f"{c.id}: {c.name}")

        elif choice == "4":
            try:
                cat_id = int(input("Enter category ID: "))
                category = Category.find_by_id(cat_id)
                if category:
                    print(f"ID: {category.id}, Name: {category.name}")
                else:
                    print("Category not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")
