# Expense Tracker CLI

A simple and efficient command-line application for tracking personal
expenses.\
This project uses **SQLite3**, **Python ORM classes**, and a
**menu-driven CLI**.

------------------------------------------------------------------------

## Features

### ✔ Core Features

-   Add, list, update, and delete expenses\
-   Add, list, update, and delete categories\
-   Automatic database creation\
-   Search and filter expenses\
-   Reporting system

### ✔ Reporting

-   Total spending\
-   Spending by category\
-   Spending over selected dates

### ✔ Search & Filter

-   Search by description\
-   Filter by date range\
-   Filter by category

------------------------------------------------------------------------

## Project Structure

    expense_tracker/
    │
    ├── db/
    │   ├── connection.py
    │   └── schema.py
    │
    ├── models/
    │   ├── category.py
    │   └── expense.py
    │
    ├── cli/
    │   ├── main_menu.py
    │   ├── expense_menu.py
    │   ├── category_menu.py
    │   ├── report_menu.py
    │   └── search_menu.py
    │
    ├── main.py
    └── README.md

------------------------------------------------------------------------

## Installation

### 1. Install Python 3.8

Use pyenv, asdf, or system installer.

### 2. Install dependencies

    pip install pypandoc

------------------------------------------------------------------------

## Running the CLI

### Step 1: Initialize the database

    python db/schema.py

### Step 2: Run the main program

    python main.py

------------------------------------------------------------------------

## How the CLI Works

You will see a main menu with the following options:

1.  Manage Expenses\
2.  Manage Categories\
3.  Reports\
4.  Search & Filter\
5.  Exit

Navigate by typing the number of your choice.

------------------------------------------------------------------------

## License

MIT License.

------------------------------------------------------------------------

## Author

Rodney Swaji
