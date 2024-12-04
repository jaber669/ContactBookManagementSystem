from operations import add_contact, view_contacts, delete_contact, search_contacts
from storage import load_contacts, save_contacts

def main_menu():
    contacts = load_contacts()  # Load contacts from the file at the start
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)  # Save before exiting
            print("Contacts saved. Exiting the program!")
            break
        else:
            print("Invalid option! Please choose again.")

if __name__ == "__main__":
    main_menu()
