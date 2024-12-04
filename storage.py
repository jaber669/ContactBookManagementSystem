import csv

FILENAME = "contacts.csv"

def load_contacts():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

def save_contacts(contacts):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['Name', 'Email', 'Phone', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
