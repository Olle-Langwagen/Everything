#Hitta nollställen

def f(x):
    return x**5 - 2*x + 1
a = -5
b = 0
while b - a > 0.001:
    m = (a + b)/2
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
print("Ekvationen har en rot x =", round(m,3))
