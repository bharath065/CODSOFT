import json

contactbook = {}

def addcontact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contactbook[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully!")

def viewcontacts():
    if not contactbook:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contactbook.items():
         print(f"Name: {name}, Phone: {details['phone']}")

def searchcontact():
    searchterm = input("Enter name or phone number to search: ")
    found = 0
    for name, details in contactbook.items():
        if searchterm.lower() in name.lower() or searchterm == details["phone"]:
            print(f"\nContact found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = 1
    if not found:
        print("Contact not found.")

def updatecontact():
    name = input("Enter the name of the contact to update: ")
    if name in contactbook:
        print("Enter new details (leave blank to keep current value):")
        phone = input(f"Current phone ({contactbook[name]['phone']}): ") or contactbook[name]['phone']
        email = input(f"Current email ({contactbook[name]['email']}): ") or contactbook[name]['email']
        address = input(f"Current address ({contactbook[name]['address']}): ") or contactbook[name]['address']
        contactbook[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def deletecontact():
    name = input("Enter the name of the contact to delete: ")
    if name in contactbook:
        del contactbook[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

def savecontacts():
    with open("contacts.json", "w") as file:
        json.dump(contactbook, file)
    print("Contacts saved successfully!")

def loadcontacts():
    global contactbook
    try:
        with open("contacts.json", "r") as file:
            contactbook = json.load(file)
    except FileNotFoundError:
        pass

def main():
    loadcontacts()
    print("Welcome to the Contact Book!")
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            addcontact()
        elif choice == "2":
            viewcontacts()
        elif choice == "3":
            searchcontact()
        elif choice == "4":
            updatecontact()
        elif choice == "5":
            deletecontact()
        elif choice == "6":
            savecontacts()
            break
        else:
            print("Invalid choice. Please try again.")

main()