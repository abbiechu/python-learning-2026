def get_integer(prompt):
    while True:
        number = input(prompt)
        try:
            return int(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
get_integer("Enter an integer: ")