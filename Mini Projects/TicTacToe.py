
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
j = 0










while True:

    firstOp = int(input("Enter the first cordinate X: "))
    secondOp = int(input("Enter the second cordinate Y: "))


    if firstOp == 1:
        if secondOp == 1:
            c = "X"
        if secondOp == 0:
            f = "X"
        if secondOp == -1:
            j = "X"
    if firstOp == 0:
        if secondOp == 1:
            b = "X"
        if secondOp == 0:
            e = "X"
        if secondOp == -1:
            h = "X"
    if firstOp == -1:
        if secondOp == 1:
            a = "X"
        if secondOp == 0:
            d = "X"
        if secondOp == -1:
            g = "X"


    
    #Board
    print("|" + str(a) + "|" + str(b) + "|" + str(c) + "|")
    print("|" + str(d) + "|" + str(e) + "|" + str(f) + "|")
    print("|" + str(g) + "|" + str(h) + "|" + str(j) + "|")
