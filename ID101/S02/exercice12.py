# exercice 12
n = int(input("donner un nombre : "))
i = 2
while n % i != 0 and i<n : 
    i +=1

if i == n :
    print(f"{n} est un nombre premier")
else :
    print(f"{n} n'est un nombre premier")