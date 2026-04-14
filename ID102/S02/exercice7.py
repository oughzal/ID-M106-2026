a = int(input("Donner l'année : "))

if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
    print("L'année", a, "est bissextile")
else:
    print("L'année", a, "n'est pas bissextile")
    