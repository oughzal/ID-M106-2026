#exercice 5
a = int(input("Donner a : "))
b = int(input("Donner b : "))
op = input("Donner l'opération (+, -, *, /) : ")

if op == '+':
    print(f"{a} + {b} = {a + b}") #f-string
    
elif op == '-':
    print(f"{a} - {b} = {a - b}")
elif op == '*':
    print(f"{a} * {b} = {a * b}")
elif op == '/':
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("division par zéro impossible")
else:
    print("opération non valide")

match op:
    case '+': print(f"{a} + {b} = {a + b}")
    case '-': print(f"{a} - {b} = {a - b}")
    case '*': print(f"{a} * {b} = {a * b}")
    case '/':
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("division par zéro impossible")
    case _: print("opération non valide")

