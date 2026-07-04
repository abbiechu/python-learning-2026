import os
while True:
    command=input("Commands: add / list / find / delete / quit")
    if command=="add":
        name=input("Name: ")
        phone=input("Phone: ")
        with open("contacts.txt","a") as file:
            file.write(f"{name},{phone}\n")
            print("Contact added.")
    elif command=="list":
        try:
            with open("contacts.txt","r") as file:
                lines=file.readlines()
                for index,line in enumerate(lines,start=1):
                    name,phone=line.strip().split(",")
                    print(f"{index}. {name} - {phone}")
        except FileNotFoundError:
            print("No contacts found.")
    elif command=="find":
        search_name=input("Enter name to find: ")
        try:
            with open("contacts.txt","r") as file:
                found=False
                for line in file:
                    name,phone=line.strip().split(",")
                    if search_name.lower() in name.lower():
                        print(f"Found:{name}-{phone}")
                        found=True
                if not found:
                    print("Contact not found.")
        except FileNotFoundError:
            print("No contacts found.")
    elif command=="delete":
        delete_name=input("Enter name to delete: ")
        try:
            with open("contacts.txt","r") as file:
                lines=file.readlines()
            with open("contacts.txt","w") as file:
                found=False
                for line in lines:
                    name,phone=line.strip().split(",")
                    if delete_name.lower() != name.lower():
                        file.write(line)
                    else:
                        found=True
                if found:
                    print("Contact deleted.")
                else:
                    print("Contact not found.")
        except FileNotFoundError:
            print("No contacts found.")
    elif command=="quit":
        print("Goodbye!")
        break
            