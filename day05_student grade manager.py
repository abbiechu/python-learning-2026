score=[]
while True:
    s=input("Enter a score (or type 'done' to finish): ")
    if s.lower()=='done':
        break
    elif s.isdigit():
        score.append(int(s))
    else:
        print("Please enter a valid integer score or 'done' to finish.")
score.sort()
print("The scores in ascending order are:", score)
average=sum(score)/len(score) 
print("The average score is:", round(average, 2))
highest=max(score)
print("The highest score is:", highest)
lowest=min(score)
print("The lowest score is:", lowest)

