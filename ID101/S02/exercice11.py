n = int(input("donner un nombre : "))
s = 0
for i in range(n, 0, -2):
    s += i
print(f"s = {s}")