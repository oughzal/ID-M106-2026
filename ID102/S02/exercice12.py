n = int(input("donner un nombre : "))

if n==1 : 
    print(f"{n} est un nombre premier")
 
i = 2
while n%i != 0 and i < n :
    i += 1
if i == n :
    print(f"{n} est un nombre premier")
else :
    print(f"{n} n'est pas un nombre premier")