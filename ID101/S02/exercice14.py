# exercice 14

n = int(input("donner un nombre : "))
s = 0
while n > 0 :
    s += n % 10
    n  = n // 10
print(f"s = {s}")