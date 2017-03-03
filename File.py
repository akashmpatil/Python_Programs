string = input("Write a few lines : ")
txt = string.split()
result = []

for words in txt:
    if len(words) < 20:
        continue
    result.append(words)

print (', '.join(result), "have GREATER  than 20 letters!")