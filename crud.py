import mysql.connector

# Step 1: Create the database if it doesn't exist
def create_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS university")
    db.close()

# Step 2: Create the table if it doesn't exist
def create_table():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="university"
    )
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            cource VARCHAR(100)
        )
    """)
    db.close()

# Step 3: Connect to the database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="university"
    )

# Step 4: Add Record
def add_record():
    db = connect_db()
    cursor = db.cursor()

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    cource = input("Enter Course: ")

    query = "INSERT INTO student (name, age, cource) VALUES (%s, %s, %s)"
    values = (name, age, cource)
    cursor.execute(query, values)

    db.commit()
    print("✅ Record added successfully.")
    db.close()

# Step 5: View Records
def view_records():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()

    print("\n📄 Student Records:")
    for record in records:
        print(record)

    db.close()

# Step 6: Update Record
def update_record():
    db = connect_db()
    cursor = db.cursor()

    student_id = int(input("Enter Student ID to update: "))
    new_cource = input("Enter new Course: ")

    query = "UPDATE student SET cource = %s WHERE id = %s"
    values = (new_cource, student_id)
    cursor.execute(query, values)

    db.commit()
    print("✅ Record updated successfully.")
    db.close()

# Step 7: Delete Record
def delete_record():
    db = connect_db()
    cursor = db.cursor()

    student_id = int(input("Enter Student ID to delete: "))

    query = "DELETE FROM student WHERE id = %s"
    cursor.execute(query, (student_id,))

    db.commit()
    print("🗑️ Record deleted successfully.")
    db.close()

# Main menu logic
create_database()
create_table()

while True:
    print("\n📋 MENU")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_record()
    elif choice == 2:
        view_records()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
    elif choice == 5:
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice. Try again.")
