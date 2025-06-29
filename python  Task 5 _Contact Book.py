# contact_book.py

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully!")

def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print("\nName:", name)
            print("Phone:", details["Phone"])
            print("Email:", details["Email"])
            print("Address:", details["Address"])
    else:
        print("No contacts found.")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print("Phone:", contacts[name]["Phone"])
        print("Email:", contacts[name]["Email"])
        print("Address:", contacts[name]["Address"])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
