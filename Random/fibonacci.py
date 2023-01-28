x0 = 0
x1 = 1
x2 = 1
xn = 0
talLista = []
tal = int(input("Tal: "))
print(x0)
for i in range(tal-1):
    x0 = x1
    x1 = x2
    x2 = xn
    xn = x0 + xn + x1
    talLista.append(xn)
    print(xn)
print(talLista)
#def rekursiv():
    #for i in range(tal-1):
    #x0 = x1
    #x1 = x2
    #x2 = xn
    #xn = x0 + xn + x1
    #pass
