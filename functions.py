import json
import os 

FILE_NAME = "data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return[]

    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return[]

def save_data(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)

def add_person():
    records = load_data()

    person_id = input("Enter Person ID: ")

    if any(person["id"] == person_id for person in records):
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")

    person = {
        "id": person_id,
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "city": city
    }
    records.append(person)
    save_data(records)

    print("Person Added Successfully!")

def view_people():
    records = load_data()

    if not records:
        print("No Records Found!")
        return
    for person in records:
        print(person)

def search_person():
    records = load_data()

    person_id = input("Enter Person ID: ")

    for person in records:
        if person["id"] == person_id:
            print("Record Found: ")
            print(person)
            return

    print("Record not Found!")

def update_person():
    records = load_data()

    person_id = input("Enter Person ID to update: ")

    for person in records:
        if person["id"] == person_id:

            print("1. Name")
            print("2. Age")
            print("3. Gender")
            print("4. Phone")
            print("5. Email")
            print("6.City")

            choice = input("Select Field: ")

            fields = {
                "1": "name", 
                "2": "age",
                "3": "gender",
                "4": "phone",
                "5": "email",
                "6": "city"
            }

            if choice in fields:
                new_value = input("Enter New Value: ")
                person[fields[choice]] = new_value
                save_data(records)
                print("Record Updated Successfully!")
            else:
                print("Invalid Selection!")

            return
    print("record Not Found!")

def delete_person():
    records = load_data()

    person_id = input("Enter Person ID to Delete: ")

    for person in records:
        if person["id"] == person_id:

            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":
                records.remove(person)
                save_data(records)
                print("Record Deleted Successfully!")
            else:
                print("Deletion Cancelled!")

            return
    print("Record Not Found! ")
               
            