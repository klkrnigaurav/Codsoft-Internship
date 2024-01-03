class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone_number']}")

    def search_contact(self, keyword):
        matches = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone_number']:
                matches.append((name, details))
        return matches

    def update_contact(self, name):
        if name in self.contacts:
            print(f"Updating contact '{name}':")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            self.contacts[name]['phone_number'] = phone_number
            self.contacts[name]['email'] = email
            self.contacts[name]['address'] = address

            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_manager.view_contact_list()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            matches = contact_manager.search_contact(keyword)
            if matches:
                print("Search Results:")
                for name, details in matches:
                    print(f"{name}: {details['phone_number']}")
            else:
                print("No matches found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_manager.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
