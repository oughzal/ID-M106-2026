from math import sqrt
a = float(input("donner a : "))
b = float(input("donner b : "))
c = float(input("donner c : "))

d = b*b - 4*a*c

if d < 0:
    print("pas de solution")
elif d == 0:
    x1 = -b / (2*a)
    print("Une solution : ", x1)
else:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print("Deux solutions : ", x1, " et ", x2)