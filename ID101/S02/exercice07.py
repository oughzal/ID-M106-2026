m = int(input("donner l'année : "))
if (m % 4 == 0 and m % 100 != 0) or (m % 400 == 0):
    print(f"{m} est une année bissextile")
else:
    print(f"{m} n'est pas une année bissextile")