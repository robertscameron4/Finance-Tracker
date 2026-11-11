from database import connect

def add_budget():

    category_id = input("Enter Category ID: ")
    monthly_limit = float(input("Enter Monthly Budget: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Budgets (CategoryID, MonthlyLimit)
        VALUES (?, ?)
    """, (category_id, monthly_limit))

    conn.commit()
    conn.close()

    print("Budget Added Successfully")

def view_budgets():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Budgets")

    budgets = cursor.fetchall()

    for budget in budgets:
        print(budget)

    conn.close()

def financial_summary():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(Amount)
        FROM Transactions
    """)

    total = cursor.fetchone()[0]

    print("\nFINANCIAL SUMMARY")
    print("Total Spending: $", total)

    conn.close()

def category_report():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT CategoryID,
               SUM(Amount)
        FROM Transactions
        GROUP BY CategoryID
    """)

    results = cursor.fetchall()

    print("\nCATEGORY REPORT")

    for row in results:
        print("Category:", row[0],
              "Total:", row[1])

    conn.close()