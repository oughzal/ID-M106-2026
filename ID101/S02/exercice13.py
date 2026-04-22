n = int(input("Donner un nombre : "))
s = 0
for i in range(1,n):
    if n%i==0 : 
        s +=i
if s== n :
    print(f"{n} est un nombre parfait")
else:
    print(f"{n} n'est pas un nombre parfait")

