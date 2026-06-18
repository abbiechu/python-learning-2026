year = int(input("Which year do you want to check? "))

# Main solution
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year.")
        else:
            print("not leap year.")
    else:
        print("leap year.")
else:
    print("not leap year.")

# Alternative one-line condition (same logic, for practice)
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("leap year.")
# else:
#     print("not leap year.")  