j = int(input("donner le jour : "))
m = int(input("donner le mois : "))
a = int(input("donner l'année : "))
if j>31 or j<1 or m>12 or m<1 :
    print("date invalide")
if j==31 and (m==2 or m==4 or m==6 or m==9 or m==11) :
    print("date invalide")
if m==2 and j==30:
    print("date invalide")
if m==2 and j==29 and (a%4!=0 or (a%100==0 and a%400!=0)) :
    print("date invalide")
else :
    print("date valide")