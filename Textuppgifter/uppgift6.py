filename = "input.txt"
file = open(filename, "w")
print("oasdj jashd ausdh asd", file=file)
file.close()
file = open(filename, "r")
blabla = file.read()
blabla2 = blabla.split()

count = {}
newWords = 0
totalWords = 0

for word in blabla2:
    totalWords += 1
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
        newWords += 1

print("Total words: ", totalWords)
print("New words: ", newWords)