# //Entrée
print("donner la valeur de a : ",end="")
a = int(input())
b = int(input("donner la valeur de b : "))

# //traitement

print("a=",a," ; b=",b)
# c = b
# b = a
# a = c
a,b = b,a
# //sortie

print("a=",a," ; b=",b)