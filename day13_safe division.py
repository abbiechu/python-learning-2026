def get_interger(prompt):
    while True:
        number = input(prompt)
        try:
            return int(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

numerator = get_interger("Enter the numerator: ")
denominator = get_interger("Enter the denominator: ")
if denominator == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = numerator / denominator
    print(f"Result: {result}")