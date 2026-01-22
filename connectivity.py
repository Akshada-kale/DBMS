from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["dbms"]
collection = db["books"]

def insert_stud():
    rollno = int(input("Enter the roll no : "))
    name = input("Enter your Name : ")
    div = input("Enter your div : ")
    
    collection.insert_one(
        {
            "rollno": rollno,
            "name" : name,
            "div" : div
        }
    )

    print("Data Inserted!")
insert_stud()

def update_stud():

    rollno = int(input("Enter the rollno to update that data : "))
    new_div = input("Enter the new divsion to update ")
    result = collection.update_one(
        {"rollno" : rollno},
        {"$set" : {"div" : new_div}}
    )


    if result.modified_count > 0:
        print("Data is updated!")
    else:
        print("No match found")
update_stud()

def display_stud():
     
    student = collection.find()
    for s in student:
        print(f"ROLLNO : {s['rollno']}, NAME : {s['name']}, DIV: {s['div']}")  
    

    print("-----")

display_stud()

def display_rollno():
     
    student = collection.find({"rollno" : {"$gt" : 50}})
    for s in student:
        print(f"ROLLNO : {s['rollno']}, NAME : {s['name']}, DIV: {s['div']}")  

display_rollno()
    
def delete_stud():
    rollno = int(input("Enter the rollno to update : "))
    result = collection.delete_one(
        {"rollno": rollno}
    )

delete_stud()



