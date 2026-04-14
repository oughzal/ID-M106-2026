
# exercice 3 : Caractère majuscule, minuscule, chiffre ou symbole
c = input("Donner un caractère : ")
if c >= 'a' and c <= 'z' :
    print("Caractère minuscule")
elif c >= 'A' and c <= 'Z' :
    print("Caractère majuscule")
elif c >= '0' and c <= '9' :
    print("Chiffre")
else :
    print("Caractère Symbole")

