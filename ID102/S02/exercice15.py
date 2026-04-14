n = int(input("Donner un nombre : "))
s = 0
r = n
while r != 0:
    s = s*10 + (r % 10)
    r = r // 10
print(f"S = {s}")