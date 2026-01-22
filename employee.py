from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["company"]             # 🔁 Use your own DB name
collection = db["employee"]        # 🔁 Collection name

# 1. Insert Employee
def insert_employee():
    empid = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))
    collection.insert_one({
        "empid": empid,
        "name": name,
        "salary": salary
    })
    print("✅ Employee inserted successfully!")

# 2. Update Salary
def update_salary():
    empid = int(input("Enter Employee ID to update salary: "))
    new_salary = int(input("Enter new salary: "))
    result = collection.update_one(
        {"empid": empid},
        {"$set": {"salary": new_salary}}
    )
    if result.modified_count > 0:
        print("✅ Salary updated successfully!")
    else:
        print("❌ No matching employee found or salary already same.")

# 3. Delete Employee
def delete_employee():
    empid = int(input("Enter Employee ID to delete: "))
    result = collection.delete_one({"empid": empid})
    if result.deleted_count > 0:
        print("✅ Employee deleted successfully.")
    else:
        print("❌ No employee found with that ID.")

# 4. Display All Employees
def display_all():
    employees = collection.find()
    print("\n--- Employee Records ---")
    for emp in employees:
        print(f"ID: {emp['empid']}, Name: {emp['name']}, Salary: {emp['salary']}")

# 5. Display Employees with Salary > 50000
def high_salary():
    employees = collection.find({"salary": {"$gt": 50000}})
    print("\n--- Employees with Salary > 50000 ---")
    for emp in employees:
        print(f"ID: {emp['empid']}, Name: {emp['name']}, Salary: {emp['salary']}")

# 6. Display Specific Employee by ID
def display_employee():
    empid = int(input("Enter Employee ID to search: "))
    emp = collection.find_one({"empid": empid})
    if emp:
        print(f"\nID: {emp['empid']}, Name: {emp['name']}, Salary: {emp['salary']}")
    else:
        print("❌ Employee not found.")

# Menu
while True:
    print("\n=== Employee Database Menu ===")
    print("1. Insert Employee")
    print("2. Update Salary")
    print("3. Display All Employees")
    print("4. Delete Employee")
    print("5. Display Employees with Salary > 50000")
    print("6. Display Specific Employee")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        insert_employee()
    elif choice == '2':
        update_salary()
    elif choice == '3':
        display_all()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        high_salary()
    elif choice == '6':
        display_employee()
    elif choice == '7':
        print("👋 Exiting the program.")
        break
    else:
        print("❌ Invalid choice. Please enter 1-7.")
