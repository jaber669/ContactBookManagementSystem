def validate_contact(name, email, phone):
    if not name.isalpha():
        print("Error: Name must only contain letters.")
        return False
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return False
    if "@" not in email or "." not in email:
        print("Error: Invalid email format.")
        return False
    return True
