n = int(input("donner un nombre : "))
s = 0
for i in range(n, -1, -2):
    s += i # s = s + i
print("la somme est : ", s)