T = float(input("Donner la tempétature : "))
if T <= 0:
    print("Solide")
elif T < 100:
    print("Liquide")
else:
    print("Gazeux")
print("Fin du programme")