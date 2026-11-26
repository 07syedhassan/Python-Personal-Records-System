
from functions import (
    add_person,
    view_people,
    search_person,
    update_person,
    delete_person
)

while True:

    print("\n================================")
    print("   PERSONAL INFORMATION SYSTEM")
    print("================================")

    print("1. Add New Person")
    print("2. View All Records")
    print("3. Search Person")
    print("4. Update Person")
    print("5. Delete Person")
    print("6. Exit")

    print("================================")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_person()

    elif choice == "2":
        view_people()

    elif choice == "3":
        search_person()

    elif choice == "4":
        update_person()

    elif choice == "5":
        delete_person()

    elif choice == "6":
        print("Thank you for using Personal Information System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
