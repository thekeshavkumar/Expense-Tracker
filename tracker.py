import pandas as pd
from datetime import datetime
from tabulate import tabulate
import os

FILE_NAME = "expenses.csv"

# Initialize the CSV if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
    df.to_csv(FILE_NAME, index=False)

def load_data():
    return pd.read_csv(FILE_NAME)

def save_data(df):
    df.to_csv(FILE_NAME, index=False)

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (e.g., food, transport, bills): ")
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    df = load_data()
    new_entry = {"Date": date, "Amount": amount, "Category": category, "Description": description}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    save_data(df)
    print("✅ Expense added successfully.")


def view_expenses():
    df = load_data()
    if df.empty:
        print("⚠️  No expenses found.")
    else:
        print(tabulate(df, headers='keys', tablefmt='grid'))

def view_by_category():
    df = load_data()
    if df.empty:
        print("⚠️  No expenses found.")
        return

    category = input("Enter category to filter by: ")
    filtered = df[df['Category'].str.lower() == category.lower()]
    if filtered.empty:
        print("⚠️  No expenses found in this category.")
    else:
        print(tabulate(filtered, headers='keys', tablefmt='grid'))

def show_summary():
    df = load_data()
    if df.empty:
        print("⚠️  No data to summarize.")
    else:
        summary = df.groupby('Category')['Amount'].sum().reset_index()
        print("📊 Expense Summary by Category:")
        print(tabulate(summary, headers='keys', tablefmt='fancy_grid'))

def main():
    while True:
        print("\n💰 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
