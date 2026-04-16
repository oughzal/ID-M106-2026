n = int(input("donner un nombre : "))
s = 0

for i in range(n, 0, -1):
    s += i * i
print("s =", s)
