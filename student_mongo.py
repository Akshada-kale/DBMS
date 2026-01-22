from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["college"]
collection = db["Student"]

def insert_student():
    rollno = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    contact = input("Enter Contact Number: ")
    dept = input("Enter Department: ")
    collection.insert_one({
        "rollno": rollno,
        "name": name,
        "address": address,
        "contact_no": contact,
        "department": dept
    })
    print("✅ Student inserted successfully!")

def update_address():
    rollno = int(input("Enter Roll Number to update address: "))
    new_address = input("Enter new address: ")
    result = collection.update_one(
        {"rollno": rollno},
        {"$set": {"address": new_address}}
    )
    if result.modified_count > 0:
        print("✅ Address updated successfully!")
    else:
        print("❌ No matching student found or address already updated.")

def display_students():
    students = collection.find()
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll No: {s['rollno']}, Name: {s['name']}, Address: {s['address']}, "
              f"Contact: {s['contact_no']}, Department: {s['department']}")

def delete_student():
    rollno = int(input("Enter Roll Number to delete: "))
    result = collection.delete_one({"rollno": rollno})
    if result.deleted_count > 0:
        print("✅ Student deleted successfully.")
    else:
        print("❌ No student found with that roll number.")

# Main Menu
while True:
    print("\n=== Student Database Menu ===")
    print("1. Insert Student")
    print("2. Update Address by Roll No")
    print("3. Display Students")
    print("4. Delete Student by Roll No")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        insert_student()
    elif choice == '2':
        update_address()
    elif choice == '3':
        display_students()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("👋 Exiting the program.")
        break
    else:
        print("❌ Invalid choice. Please enter 1-5.")
