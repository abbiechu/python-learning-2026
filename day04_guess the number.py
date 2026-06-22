import random
target=random.randint(1,100)
counter=0
while True:
    counter=counter+1
    guess=int(input("Guess the number between 1 and 100: "))
    if guess<target:
        print("Too low. Try again.")
    elif guess>target:
        print("Too high. Try again.")
    else:
        print("Congratulations! You guessed the number.")
        print("You have guessed",counter,"times.")
        break


