contacts={}

while True:
    print('\n Contact Book')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search conatct')
    print('Exit')

    choice=int(input("Enter your choice"))

    if choice == 1:
        name=input("Enter your name")
        if name in contacts:
            print(f'Contact name {name} already present')
        else:
            Phone_Number=int(input("Enter your phone number"))
            email=input("Enter your email")
            address=input("Enter your address")
            contacts[name] = {"Phone_Number:":int(Phone_Number),"email:":email,"address:":address}
            print(f'Contact name {name} has been create successuflly ')
    elif choice == 2:
        name=input("Enter name to view contact: ")
        if name in contacts:
            contact=contacts[name]
            print(f"Name: {name}, Phone_Number:{Phone_Number}")
        else:
            print('Contact not found')
    elif choice == 3:
        name=input("Enter name to update contact: ")
        if name in contacts:
            Phone_Number=int(input("Enter update phone number"))
            email=input("Enter update email")
            address=input("Enter uodate address")
            contacts[name]={"Phone_Number:":int(Phone_Number),"email:":email,"address:":address}
        else:
            print("Contact is not found")
    elif choice == 4:
        name=input("Enter name to Delete contact: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been delete ")
        else:
            print("Contact is not found")
    elif choice == 5:
        serach_name=input("Enter name to serach contact details ")
        found=False
        for name,contact in contacts.items():
            if serach_name.lower() in name.lower():
                print(f"found Name : {name},'Phone_Number:'{Phone_Number},'email:'{email},'address:'{address}")
                found=True
        if not found:
            print("NO Contact found")
    elif choice == 6:
        print("exit")
        break
    else:
        print("Result is not found")
        break
        
            
            
