
from database import connect


def view_transactions():
    conn = connect()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                TransactionID,
                AccountID,
                CategoryID,
                Amount,
                TransactionDate,
                Description
            FROM Transactions
            ORDER BY TransactionDate DESC
        """)

        rows = cursor.fetchall()

        if not rows:
            print("\nNo transactions found yet.")
            return

        print("\n--- YOUR TRANSACTIONS ---")
        print("-" * 85)
        print(
            f"{'ID':<6}{'Account':<10}{'Category':<10}"
            f"{'Amount':<12}{'Date':<15}Description"
        )
        print("-" * 85)

        for row in rows:
            transaction_id, account_id, category_id, amount, date, description = row

            print(
                f"{transaction_id:<6}{account_id:<10}{category_id:<10}"
                f"{amount:<12.2f}{str(date):<15}{description or ''}"
            )

    except Exception as error:
        print(f"Error retrieving transactions: {error}")

    finally:
        conn.close()

def add_transaction():
    conn = connect()

    try:
        cursor = conn.cursor()

        print("\n--- ADD TRANSACTION ---")

        transaction_type = input("Income or Expense? ").strip().lower()

        if transaction_type not in ("income", "expense"):
            print("Please enter Income or Expense.")
            return

        try:
            amount = float(input("Enter amount: $"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        cursor.execute("SELECT AccountID FROM Accounts")
        accounts = cursor.fetchall()

        if not accounts:
            print("No accounts exist yet. We need to create an account first.")
            return

        print("\nAvailable accounts:")
        for account in accounts:
            print(f"Account ID: {account[0]}")

        try:
            account_id = int(input("Enter account ID: "))
        except ValueError:
            print("Invalid account ID.")
            return

        if not any(account[0] == account_id for account in accounts):
            print("Account not found.")
            return

        cursor.execute("SELECT CategoryID, CategoryName FROM Categories")
        categories = cursor.fetchall()

        if not categories:
            print("No categories exist yet. We need to create a category first.")
            return

        print("\nAvailable categories:")
        for category in categories:
            print(f"{category[0]}: {category[1]}")

        try:
            category_id = int(input("Enter category ID: "))
        except ValueError:
            print("Invalid category ID.")
            return

        if not any(category[0] == category_id for category in categories):
            print("Category not found.")
            return

        transaction_date = input("Enter date (YYYY-MM-DD): ").strip()
        description = input("Enter description: ").strip()

        if transaction_type == "expense":
            amount = -amount

        cursor.execute("""
            INSERT INTO Transactions
                (AccountID, CategoryID, Amount, TransactionDate, Description)
            VALUES (?, ?, ?, ?, ?)
        """, (
            account_id,
            category_id,
            amount,
            transaction_date,
            description
        ))

        conn.commit()
        print("Transaction added successfully!")

    except Exception as error:
        print(f"Error adding transaction: {error}")

    finally:
        conn.close()
    

def create_account():
    conn = connect()

    try:
        cursor = conn.cursor()

        print("\n--- CREATE ACCOUNT ---")

        account_name = input("Enter account name (e.g. Checking): ").strip()

        if not account_name:
            print("Account name cannot be empty.")
            return

        try:
            balance = float(input("Enter starting balance: $"))

            if balance < 0:
                print("Starting balance cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid amount.")
            return

        cursor.execute("SELECT UserID FROM Users LIMIT 1")
        user = cursor.fetchone()

        if user is None:
            print("No user exists yet. We need to create a user first.")
            return

        cursor.execute("""
            INSERT INTO Accounts (UserID, AccountName, Balance)
            VALUES (?, ?, ?)
        """, (user[0], account_name, balance))

        conn.commit()
        print(f"Account '{account_name}' created successfully!")

    except Exception as error:
        print(f"Error creating account: {error}")

    finally:
        conn.close()
