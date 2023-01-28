#1

def tal(tal):
    rev = 0
    if tal > 0:
        while tal > 0:
            rev *= 10
            rev += tal %10
            tal //= 10
        
    else:
        while tal > 0:
            rev *= 10
            rev += tal %10
            tal //= 10
        rev *=-1
        print(tal)


print(tal(-1348))

"""
#2
def tal2(tal):
    rev= int(str(tal)[::-1])
    print(rev)
tal2(1358)

def tal(tal):
    rev = 0
    while tal > 0:
        rev *= 10
        rev += tal %10
        tal //= 10
    return rev
    print(tal)
print(tal(1348))
"""
