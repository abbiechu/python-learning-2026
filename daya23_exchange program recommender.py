school_information = [ {"school_name": "NTU", "lowest_GPA": 3.5,"lowest_TOEIC":800},
                    {"school_name": "NCTU", "lowest_GPA": 3.3,"lowest_TOEIC":750},
                    {"school_name": "NTHU", "lowest_GPA": 3.3,"lowest_TOEIC":750},
                    {"school_name": "NCKU", "lowest_GPA": 3.0,"lowest_TOEIC":700},
                    {"school_name": "NSYSU", "lowest_GPA": 3.0,"lowest_TOEIC":650},
                    {"school_name": "NCHU", "lowest_GPA": 2.8,"lowest_TOEIC":600} ]

def check_eligibility(GPA, TOEIC):
    user_GPA = float(GPA)
    user_TOEIC = int(TOEIC)
    eligibility=[]
    for school_name in school_information:
        if user_GPA >= school_name["lowest_GPA"] and user_TOEIC >= int(school_name["lowest_TOEIC"]):
            eligibility.append(school_name["school_name"])
    return eligibility

def main():
    while True:
        command = input("Enter command:check/list/quit: ")
        if command == "check":
            try:
                GPA = input("Enter your GPA: ")
                TOEIC = input("Enter your TOEIC score: ")
                eligibility = check_eligibility(GPA, TOEIC)
                if eligibility:
                    print("Eligible schools: ")
                    for school in eligibility:
                        print(school)
                else:
                    print("No eligible schools found.")
            except ValueError:
                print("Invalid input. Please enter numeric values for GPA and TOEIC.")
        elif command == "list":
            for school in school_information:
                print(f"{school['school_name']}: GPA {school['lowest_GPA']}, TOEIC {school['lowest_TOEIC']}")
        elif command == "quit":
            print("Goodbye!")
            break

main()
