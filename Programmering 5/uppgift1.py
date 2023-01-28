#num = int(input("Input: "))
primList = []
"""
for j in range(num):

    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                num-=1
                pass
        else:
            primList.append(num)
            num-=1
    else:
        pass
else:
    num-=1
    pass
primList.reverse()
print(primList)
"""
sortedList = []
num = 6
count = 0
def primeMaker(num, count):
    for num in range(2, count):
        if all(num%i!=0 for i in range(2,num)):
            primList.append(num)
            for i in range(count*2):
                if len(primList) <= num:
                    num +=1
                    print(num)

primeMaker(10, 10)
print(primList)
print(num)
"""
prime = 0
def primeMaker(num):
    for i in range(2, 38):
        if all(num%i!=0 for i in range(2,num)):
            primList.append(num)
            

primeMaker(num = int(input("Prime: ")))
print(primList)
"""
"""

for i in range(len(primList)):
    if num == primList[j+1]:
        print("Hittat")
"""