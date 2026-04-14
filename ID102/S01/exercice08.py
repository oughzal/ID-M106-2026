#Entrée
h = int(input("heures : "))
m = int(input("minutes : "))
s = int(input("secondes : "))
d = int(input("Duree en secondes : "))
# ecrire(h,":",m,":",s,"+",d ,"sec = ")
print(h,":",m,":",s,"+",d ,"sec = ",end="")
# // Traitement
s = s + d
m = m + s // 60
s = s % 60
h = h + m // 60
m = m % 60
# ecrireln(h,":",m,":",s)
print(h,":",m,":",s)