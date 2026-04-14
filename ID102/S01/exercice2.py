# // Entrée
Q = int(input("donner la quantité : "))
PU = float(input("donner le prix unitaire : "))
# // Traitement
HT  = Q * PU
TTC = HT * (1 + 0.2)
# // Sortie

print("le prix TTC : ", TTC)