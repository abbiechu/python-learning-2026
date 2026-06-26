contact={}
while True:
    command=input("Enter command (add, find, quit, list): ")
    if command=="add":
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        contact[name]=phone
    elif command=="find":
        name=input("Enter name to find: ")
        if name in contact:
            print(f"Phone number for {name} is {contact[name]}")
        else:
            print(f"{name} not found in contacts.")
    elif command=="list":
        print("Contacts:")
        for name, phone in contact.items():
            print(f"{name}: {phone}")
    elif command=="quit":
        break
    else:
        print("Invalid command.")
