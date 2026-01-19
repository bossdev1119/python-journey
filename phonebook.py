phonebook ={}

def add_contact(name , phone):
   phonebook[name]= phone

def search_contact(contact):
    if contact in phonebook:
        return phonebook[contact]
    elif int(contact) in phonebook.values():
        for name, phone in phonebook.items():
            if phone == contact:
                break
        return phonebook[name]
    else:
        return None
    
    
def delete_contact(contact):
    if contact in phonebook:
        del phonebook[contact] 
        return True
    elif int(contact) in phonebook.values():
        for name, phone in phonebook.items():
            if phone == contact:
                del phonebook[name]
            return True
    else:
        return None

while True:
        print(''' 
        1. Add Contact
        2.Search Contact
        3.Delete Contact
        4.View All Contacts
        5.Exit Phonebook App\n''')

        userInput= int(input("Choose an option: "))
        if userInput==1:
            name = input("Enter contact name: ")
            while True:
                try:
                    phone = int(input("Enter contact phone number: "))
                    if len(str(phone))==10 :
                        add_contact(name,phone)
                        print("added successfully")
                        break
                    else:
                       print("OOps! Phone must be 10 digits")

                except ValueError:
                    print("Invalid phone number!")
        elif userInput==2:
            contact= input("search: ")
            result= search_contact(contact)
            if result is not None:
                if contact in phonebook:
                    print(f"Contact found:\n {contact} : {result}")
                    
                else:
                    print(f"Contact found:\n {name} : {result}")
            else:
                print("Contact not found")

        elif userInput==3:
            contact= input("Enter contact: ")
            result = delete_contact(contact)
            if result is not None:
                print(f"Contact {contact} deleted successfully")
            else:
                print("Contact not found")

        elif userInput==4:
            print("All Contacts:")
            for name , phone in phonebook.items():
                print(f"{name} : {phone}")
        elif userInput==5:
            print("Exiting Phonebook App. Goodbye!")
            break