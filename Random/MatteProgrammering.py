"""
x1 = -1
y1 = 1
x2 = 2
y2 = 5

a1 = -1
b1 = 1
a2 = 2
b2 = 5

e = ((a2 - a1)**2 + (b2 - b1)**2)**0.5

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x = (x1 + x2)/2
y = (y1 + y2)/2

kVärdet1 = ((y2 - y1)/(x2 - x1))
kVärdet2 = ((b2 - b1)/(a2 - a1))

if(e == d):
    print("Sträckorna är lika långa!")
else:
    print("avstånd sträcka 1:", round(d, 2), "l.e.", "\n avstånd sträcka 2:", round(e, 2), "l.e.")

if(kVärdet1 == kVärdet2):
    print("Sträckorna är parallela!")
else:
    print("K-Värdet sträcka 1: ", kVärdet1, "\nK-Värdet sträcka 2: ", kVärdet2)

if(kVärdet1*kVärdet2 == -1):
    print("De är vinkelräta")
else:
    print("Sträckorna är inte vinkelräta")
print("mittpunkt", (x, y))
"""

##Triangel

x1 = -2
x2 = 0
x3 = 2

y1 = -2
y2 = 4
y3 = -2

d1 = ((x1-x2) + (y1-y2))
d2 = ((x2-x3) + (y2-y3))
d3 = ((x3-x1) + (y3-y1))

if(d1 == d2 == d3):
    print("liksidig")
else:
    print("Inte liksidig")
    print(d1, d2, d3)
