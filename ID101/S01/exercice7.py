# //Entrée

t = int(input("donner le nombre de secondes : "))
# //Traitement
h = t // 3600
t = t % 3600
m = t // 60
s = t % 60
# //Sortie
# ecrire(h,":",m,":",s)
print(h,":",m,":",s)
print(f"{h}:{m}:{s}") # f-string