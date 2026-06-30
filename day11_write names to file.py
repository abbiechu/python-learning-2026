with open("names.txt","w") as file:
    while True:
        name=input("Enter a name (or 'done' to finish): " )
        if name=="done":
            break
        file.write(name+"\n")