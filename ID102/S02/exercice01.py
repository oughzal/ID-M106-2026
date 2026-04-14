t = float(input("Donner une température en degrés Celsius : "))

if t < 0 :
    print("Solide")
elif t < 100 :
    print("Liquide")
else :
    print("Gazeux")
print("Fin du programme")