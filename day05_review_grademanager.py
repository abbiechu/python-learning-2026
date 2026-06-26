score=[]
while True:
    s=input("Enter a score (or 'quit' to finish): ")
    if s.lower()=="quit":
        break
    elif not s.isdigit():
        print("Invalid input. Please enter a valid score.")
        continue
    score.append(int(s))
score.sort()
print("The scores in ascending order are:", score)
average=sum(score)/len(score)
print("The average score is:", round(average, 2))
maximum=max(score)
print("The highest score is:", maximum)
minimum=min(score)
print("The lowest score is:", minimum)
