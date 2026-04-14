n = int(input("donner un nombre : "))
s = 0
for i in range(n,2,-1):
    s += i * i
print("la somme est :", s)