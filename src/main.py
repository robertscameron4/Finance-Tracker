
from database import connect
from transaction_manager import view_transactions, add_transaction, create_account
from budget_manager import add_budget, view_budgets, financial_summary
from user_manager import create_user
from category_manager import create_category

conn = connect()
print("Database Connected Successfully")
conn.close()

while True:
    print("\nPERSONAL FINANCIAL TRACKER")
    print("1. Create User Account")
    print("2. Create Category")
    print("3. View Transactions")
    print("4. Add Transaction")
    print("5. Create Account")
    print("7. Add Budget")
    print("8. View Budgets")
    print("9. Financial Summary")
    print("10. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        create_user()

    if choice == "2":
        create_category()

    if choice == "3":
        view_transactions()

    elif choice == "4":
        add_transaction()

    elif choice == "5":
        create_account()

    elif choice == "7":
        add_budget()

    elif choice == "8":
        view_budgets()

    elif choice == "9":
        financial_summary()

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
