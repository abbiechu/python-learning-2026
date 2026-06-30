with open("names.txt","r") as file:
    lines=file.readlines()
    print(f"Number of lines: {len(lines)}")
    for index,line in enumerate(lines,start=1):
        print(f"{index}: {line.strip()}")