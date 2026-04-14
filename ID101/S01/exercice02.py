# // Entrée
Qt = int(input("donner la quantité : "))
PU = float(input("donner le prix unitaire : "))
# // Traitement
TVA = 0.2
TTC = Qt * PU * (1 + TVA)
# // Sortie
print("le prix TTC : ", TTC)