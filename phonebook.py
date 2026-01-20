phonebook ={}

def add_contact(name , phone):
   phonebook[name]= phone

def searchName(contact_search):
    if contact_search in phonebook:
        return name , phonebook[contact_search]
    else:
        return None
    
def searchContact(contact_search):
    if contact_search in phonebook.values():
        for name ,phone in phonebook.items():
            if phone ==contact_search:
                return name, phonebook[name]
    else:
        return None
    

    
    
def delete_contact(contact_delete):

    if contact_delete in phonebook:
        del phonebook[contact_delete] 
        return True
    
    if contact_delete.isdigit():
        contact_delete=int(contact_delete)
        for name,phone in phonebook.items():
            if phone==contact_delete:
                del phonebook[name]
                return True 
        

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
            contact_search= input("search: ")
            if contact_search.isdigit():
                contact_search= int(contact_search)
                result= searchContact(contact_search)
                
                if result : #asking question if function found something 
                    name , phone = result 
                    print(f"Contact found:\n {name} : {phone}")
                else:
                    print("Contact not found")
            else:
                result= searchName(contact_search)
                
                if result :
                    name,phone = result
                    print(f"Contact found:\n {name} : {phone}")
                else:
                    print("Contact not found")

        elif userInput==3:
            contact_delete= input("Enter contact: ")
            confirm =input("do you really want to delete this contact? y/n ")
            if confirm=='y'or confirm=='Y':
                result=delete_contact(contact_delete)
                if result : # asking question if function found something 
                    print("Contact deleted successfully")
                else:
                    print("Contact not found")
            else:
                break

        elif userInput==4:
            print("All Contacts:")
            for name , phone in phonebook.items():
                print(f"{name} : {phone}")
        elif userInput==5:
            print("Exiting Phonebook App. Goodbye!")
            break