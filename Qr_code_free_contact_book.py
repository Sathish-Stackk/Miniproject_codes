contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    print(name, ":", contacts.get(name, "Contact not found"))

def show_contacts():
    for name, phone in sorted(contacts.items()):
        print(f"{name}: {phone}")

add_contact("Sathish", "9876543210")
add_contact("Rahul", "9123456780")

search_contact("Sathish")
show_contacts()
