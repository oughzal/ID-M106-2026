# exercice9
def estPremier(n):
    if n<=2 :
        return True
    for i in range(2,n):
        if n%i==0 : 
            return False
    return True

print(estPremier(1))
print(estPremier(2))
print(estPremier(7))
print(estPremier(18))