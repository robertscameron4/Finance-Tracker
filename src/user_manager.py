from database import connect

def create_user():

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Users
        (FirstName, LastName, Email)
        VALUES (?, ?, ?)
    """, (first_name, last_name, email))

    conn.commit()

    print("User Created Successfully")

    conn.close()