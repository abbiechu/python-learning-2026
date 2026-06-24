dict={}
while True:
    command=input("Enter command: ")
    if command=="quit":
        print("Goodbye!")
        break
    elif command=="add":
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        dict[name]=phone
        print("Added.")
    elif command=="find":
        name=input("Enter name: ")
        if name in dict:
            print(name,"'s phone number is: ",dict[name],sep="")
        else:
            print(name,"Not found.")
    elif command=="list":
        if dict:
            for name,phone in dict.items():
                print(name,":",phone)
        else:
            print("Contact list is empty.")

    


