from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["collage"]
collection=db["student"]
def insert_student():
    r=int(input("enter the roll no"))
    n=input("enter the name")
    a=input("enter the name")
    c=input("enter the name")
    d=input("enter the name")
    collection.insert_one(
        {
            "rollno":r,
            "name":n,
            "address":a,
            "dep":d,
            "con":c
        }
    )
    print("insert done")
def update_student():
    r=int(input("enter the roll no"))
    a=input("enter the name")
    collection.update_one(
        {"rollno":r},
        {"$set":{"address":a}}
    )
    print("update done")
def delete_student():
    r=int(input("enter the name"))
    collection.delete_one(
        {"rollno":r}
    )
    print("delete")
def display_student():
    stud=collection.find()
    for s in stud:
        print(f" name: {s['name']} ,roll {s['rollno']}  ,,address : {s['address']}")
def display_per():
    r=int(input("enter the name"))
    stud=collection.find({"rollno":r})
    for s in stud:
        print(f" name: {s['name']} ,roll {s['rollno']}  ,,address : {s['address']}")
while True:
    print("1 in")
    print("2 up")
    print("3 de")
    print("4 dis")
    print("5")
    ch=int(input("enter the choice"))
    if ch==1:
        insert_student()
    elif ch==2:
        update_student()
    elif ch==3:
        delete_student()
    elif ch==4:
        display_student()
    elif ch==5:
        display_per()
    else:
        print("the worhf")
