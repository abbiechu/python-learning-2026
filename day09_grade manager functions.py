def add_grade(grades, grade):
    grades.append(float(grade))
    return grades
def sort_grades(grades):
    return sorted(grades)
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)
def find_highest_grade(grades):
    if len(grades) == 0:
        return None
    return max(grades)
def find_lowest_grade(grades):
    if len(grades) == 0:
        return None
    return min(grades)
def main():
    grades = []
    while True:
        grade = input("Enter a grade (or 'done' to finish): ")
        if grade == "done":
            break
        print(f"Grades: {add_grade(grades, grade)}")
    print(f"Sorted Grades: {sort_grades(grades)}")
    print(f"Average Grade: {round(calculate_average(grades),2)}")
    print(f"Highest Grade: {find_highest_grade(grades)}")
    print(f"Lowest Grade: {find_lowest_grade(grades)}") 
main()