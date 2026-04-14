from math import gcd
n = int(input("Donner le numérateur : "))
d = int(input("Donner le dénominateur : "))
i = n if n>d else d
while n % i != 0 or d % i != 0:
    i -= 1
print(f"{n}/{d} = {n // i}/{d // i}")

i = gcd(n, d)
print(f"{n}/{d} = {n // i}/{d // i}")