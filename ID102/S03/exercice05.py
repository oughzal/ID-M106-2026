# exercice 5
def max3(a,b,c):
    m = a
    if b > m : 
        m = b
    if c > m : 
        m = c
    return m
    return max(a,b,c)

print(max3(3,5,7))
