n = int(input("donner un nombre : "))
f = 1 
for i in range(1,n+1):
    f *= i
print(f"{n}! = {f}")  # f-string formatting
print(n, "! = ", f)