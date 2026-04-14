#exercice 4 : Résolution d'une équation du second degré
from math import sqrt
a = float(input("Donner la valeur de a : "))
b = float(input("Donner la valeur de b : "))
c = float(input("Donner la valeur de c : "))

d = b**2 - 4*a*c

if d < 0:
    print("Pas de solution réelle")
elif d == 0:
    x1 = -b / (2*a)
    print("Solution double :", x1)
else:
    x1 = (-b - sqrt(d)) / (2*a)
    x2 = (-b + sqrt(d)) / (2*a)
    print("Solutions :", x1, "et", x2)