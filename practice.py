from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["neha"]
collection = db["emp"]


def insert_emp():
    emp_id = int(input("Enter the employee ID: "))
    name = input("Enter Name : ")


    collection.insert_one(
        {
            "emp_id": emp_id,
            "name": name
        }
    )

    print("Data inserted!")

insert_emp()

def update_emp():
    emp_id = int(input("Enter the employee Id to update : "))
    new_name = input("Enter the new name : ")

    result = collection.update_one(
        {"emp_id":emp_id},
        {"$set" : {"name" : new_name}}
    )

    if result.modified_count>0:
        print("Data updated!")
    else:
        print("No match found")

update_emp()


def display_emp():

    emp = collection.find()
    for e in emp:
       print(f"NAME : {e['name']}, EMPLOYEE_ID: {e['emp_id']}" )

display_emp()


def delete_emp():
     
    emp_id = int(input("Enter the employee id to delete : "))
    result = collection.delete_one(
        {"emp_id" : emp_id}
    )
    if result.deleted_count>0:
        print("Data Deleted!")
    else:
        print("No match found!")

    
delete_emp()

