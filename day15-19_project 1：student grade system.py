import os
def load_grades():
    grade={}
    if os.path.exists("grades.txt"):
        with open("grades.txt","r") as file:
            for line in file:
                name,score=line.strip().split(",")
                grade[name]=int(score)
    return grade
def save_grades(grade):
    with open("grades.txt","w") as file:
        for name,score in grade.items():
            file.write(f"{name},{score}\n")
def get_integer(prompt):
    while True:
        try:
            value=int(input(prompt))
            return value
        except ValueError:
            print("Invalid input.Please enter an integer.")
def main():
    grade=load_grades()
    while True:
        command=input("Commands: add / list / average / highest / lowest /find / delete / quit: ")
        if command=="add":
            name=input("Name: ")
            score=get_integer("Score: ")
            grade[name]=score
            print("Added.")
        elif command=="list":
            if not grade:
                print("No grades found.")
            else:
                for name,score in grade.items():
                    print(f"{name} - {score}")
        elif command=="average":
            if not grade:
                print("No grades found.")
            else:
                average=sum(grade.values())/len(grade)
                print(f"Average score: {round(average, 2)}")
        elif command=="highest":
            if not grade:
                print("No grades found.")
            else:
                highest_name=None
                highest_grade=-1
                for name,score in grade.items():
                    if score>highest_grade:
                        highest_grade=score
                        highest_name=name
                highest_grade=grade[highest_name]
                print(f"Highest score:{highest_name}-{highest_grade}")
        elif command=="lowest":
            if not grade:
                print("No grades found.")
            else:
                lowest_name=None
                lowest_grade=101
                for name,score in grade.items():
                    if score<lowest_grade:
                        lowest_grade=score
                        lowest_name=name
                lowest_grade=grade[lowest_name]
                print(f"Lowest score:{lowest_name}-{lowest_grade}")
        elif command=="find":
            search_name=input("Enter name to find:")
            if search_name in grade:
                print(f"Found:{search_name}-{grade[search_name]}")
            else:
                print("Student not found.")
        elif command=="delete":
            delete_name=input("Enter name to delete:")
            if delete_name in grade:
                del grade[delete_name]
                print("Deleted.")
            else:
                print("Student not found.")
        elif command=="quit":
            save_grades(grade)
            print("Goodbye!")
            break
main()   