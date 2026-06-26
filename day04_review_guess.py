import random
target=random.randint(1, 100)
count=0
while True:
    guess=int(input("Enter your guess: "))
    count += 1
    if guess<target:
        print("Too low!")
    elif guess>target:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {count} guesses.")
        break