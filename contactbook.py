contacts = []

def add_contact():
    print("\n Add New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(" Contact added successfully!")

def view_contacts():
    print("\n Contact List")
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n Search Contact")
    search = input("Enter name or phone: ").lower()

    found = False
    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone']:
            print("\n Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print(" No matching contact found.")

def update_contact():
    view_contacts()
    if not contacts:
        return

    try:
        choice = int(input("\nEnter contact number to update: ")) - 1
        if 0 <= choice < len(contacts):
            contact = contacts[choice]

            print("\n Update Contact (leave blank to keep old value)")
            name = input(f"New Name ({contact['name']}): ") or contact['name']
            phone = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New Email ({contact['email']}): ") or contact['email']
            address = input(f"New Address ({contact['address']}): ") or contact['address']

            contacts[choice] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            print(" Contact updated!")
        else:
            print(" Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return

    try:
        choice = int(input("\nEnter contact number to delete: ")) - 1
        if 0 <= choice < len(contacts):
            deleted = contacts.pop(choice)
            print(f" Deleted {deleted['name']} successfully!")
        else:
            print(" Invalid choice.")
    except ValueError:
        print(" Please enter a valid number.")

def menu():
    while True:
        print("\n======  CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid option. Try again.")

# Run program
if __name__ == "__main__":
    menu()