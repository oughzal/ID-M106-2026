#Exercice 2 : Vérification de la validité d'une note
note = float(input("Donner la note : "))
if note >= 0 and note <= 20 :
    print("la note est valide")
else :
    print("la note est invalide")
if 0 <= note <= 20 :
    print("la note est valide")
else :
    print("la note est invalide")
