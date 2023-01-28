input = input(str("Input: "))
find = ([pos for pos, char in enumerate(input) if char == "-"])
list = find
count = 0
count2 = 0
text = 0
output = input[0]

for i in range(len(list)):
    count2 = find[count]
    text = (input[count2 + 1])
    count+=1
    output = output + text
    
print(output)