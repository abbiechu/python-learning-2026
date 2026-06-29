sentence=[]
while True:
    word=input("Enter a word (or 'done' to finish): ")
    if word == "done":
        break
    sentence.append(word)

print(" ".join(sentence))
