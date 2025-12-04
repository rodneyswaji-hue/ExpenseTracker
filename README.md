# Expense Tracker CLI

A command-line application built with Python, SQLite, and custom ORM methods.  
The app allows users to manage **Categories** and **Expenses**, enforcing a one-to-many relationship.

---

## 📌 Features

### ✔ Category Management
- Create a category  
- Delete a category  
- View all categories  
- Find a category by ID  
- View expenses related to a category  

### ✔ Expense Management
- Create an expense  
- Delete an expense  
- View all expenses  
- Find an expense by ID  

### ✔ Data Model
The project includes:
- **Category** (one)
- **Expense** (many)

Relationship:
`One Category → Many Expenses`

### ✔ ORM Methods Implemented
Each model contains:
- `create()`
- `get_all()`
- `find_by_id()`
- `delete()`

### ✔ Input Validation (Property Methods)
- Categories must have a non-empty string name  
- Expenses:
  - Amount must be positive  
  - Date must be in `YYYY-MM-DD` format  
  - Category ID must be integer  

---

## 📂 Project Structure

