from utils import validate_contact

def add_contact(contacts):
    print("--- Add Contact ---")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    # Validate and check for duplicates
    if not validate_contact(name, email, phone):
        return
    if phone in [c['Phone'] for c in contacts]:
        print("Error: Phone number already exists.")
        return

    # Add to contacts
    contacts.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
    print("Contact added successfully!")

def view_contacts(contacts):
    print("--- View Contacts ---")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}")

def delete_contact(contacts):
    print("--- Delete Contact ---")
    phone = input("Enter the phone number of the contact to delete: ")
    for contact in contacts:
        if contact['Phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Error: Contact not found.")

def search_contacts(contacts):
    print("--- Search Contacts ---")
    query = input("Enter a search term (Name, Phone, Email, or Address): ")
    results = [c for c in contacts if query.lower() in str(c.values()).lower()]
    if results:
        print("Search Results:")
        for contact in results:
            print(f"{contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}")
    else:
        print("No contacts found.")
