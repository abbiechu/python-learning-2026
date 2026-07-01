import os
while True:
    command=input("Commands: new / list / read / delete / quit")
    if command=="new":
        title=input("Title: ")
        content=input("Content: ")
        with open(title+".txt","w") as file:
            file.write(content)
            print("Note saved.")
    elif command=="list":
        txt_files = []
        for f in os.listdir("."):
            if f.endswith(".txt"):
                txt_files.append(f)
        for i, file in enumerate(txt_files, start=1):
            print(f"{i}. {file.replace('.txt', '')}")
    elif command=="read":
        title=input("Title: ")
        if not os.path.exists(title+".txt"):
            print("Note not found.")
        else:
            with open(title+".txt","r") as file:
                content=file.read()
                print(content)
    elif command=="delete":
        title=input("Title:")
        if not os.path.exists(title+".txt"):
            print("Note not found.")
        else:
            os.remove(title+".txt")
            print("Deleted.")
    elif command=="quit":
        print("Goodbye!")
        break
