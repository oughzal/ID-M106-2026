a = int(input("Donner a : "))
b = int(input("Donner b : "))
op = input("Donner l'opération (+, -, *, /) : ")

if op == '+':
    print("Résultat :", a + b)
elif op == '-':
    print("Résultat :", a - b)
elif op == '*':
    print("Résultat :", a * b)
elif op == '/':
    if b == 0:
        print("Erreur : division par zéro")
    else:
        print("Résultat :", a / b)
else:
    print("Opération non valide")

match op:
    case '+': print("Résultat :", a + b)
    case '-': print("Résultat :", a - b)
    case '*': print("Résultat :", a * b)
    case '/':
        if b == 0:
            print("Erreur : division par zéro")
        else:
            print("Résultat :", a / b)
    case _: print("Opération non valide")