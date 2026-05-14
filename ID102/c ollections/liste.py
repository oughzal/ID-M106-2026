L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2 + [7,8,9]
print(L3)
L4 = L1 * 3 # L1 * 3 = L1 + L1 + L1
print(L4)
print("*"*10)
print(5 in L1)

v = int(input("Entrez un nombre: "))
if v in L1:
    print("Le nombre est dans la liste")
else:
    print("Le nombre n'est pas dans la liste")