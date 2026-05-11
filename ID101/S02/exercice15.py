# exercice 15

n = int(input("donner un nombre : "))
r = 0
while n > 0 :
    r = r*10 + n%10
    n //=10
print(f"l'inverse  est {r}")