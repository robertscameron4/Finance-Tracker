from database import connect

def create_category():

    category_name = input("Enter Category Name: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Categories (CategoryName)
        VALUES (?)
    """, (category_name,))

    conn.commit()

    print("Category created successfully!")

    conn.close()
