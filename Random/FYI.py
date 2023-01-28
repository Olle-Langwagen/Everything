nummer = str(input("Number: "))
count = 0
fem = 0
for i in range(0,3):
    if nummer[count] == "5":
        fem = 5
        count+=1
if count == 3:
    print(1)
else:
    print(0)