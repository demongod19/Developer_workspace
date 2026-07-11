contacts = {
    "John Doe": {
        "phone": "123-456-7890",
        "email": "john.doe@example.com"
    }
}
while True:
    print("1. Display Contact Details")
    print("2. Add Contact Details")
    print("3. Update Contact Details")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
     if not contacts:
        print("No contacts available.")
     else:
        print("\nContacts")
        print("-" * 40)
        for name, details in contacts.items():
            print(f"Name : {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 40)
    elif choice == '2':
        contact_name = input("Enter contact name: ")
        if contact_name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Phone: ")
            email = input("Email: ")
            contacts[contact_name] = {
                "phone": phone,
                
        "email": email
            }
            print("Contact added successfully.")    
            print("New contact added successfully.")
    elif choice == '3':
        contact_name = input("Enter contact name: ")
        if contact_name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[contact_name]['phone'] = new_phone
            new_email = input("Enter new email address: ")
            contacts[contact_name]['email'] = new_email
            print("Contact details updated successfully.")
        else:
            print("Contact not found.")
    elif choice == '4':
        contact_name = input("Enter contact name to delete: ")
        if contact_name in contacts:
            del contacts[contact_name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == '5':
        contact_name = input("Enter contact name to search: ")
        if contact_name in contacts:
            print(f"Contact Name: {contact_name}")
            print(f"Phone Number: {contacts[contact_name]['phone']}")
            print(f"Email Address: {contacts[contact_name]['email']}")
        else:
            print("Contact not found.")
    elif choice == '6':
        print("Exiting the program.")
        break