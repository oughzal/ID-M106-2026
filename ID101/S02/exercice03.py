c = input("Donner un caractère : ")
if 'a' <= c <= 'z':
    print("Caractère minuscule")
elif 'A' <= c <= 'Z':
    print("Caractère majuscule")
elif '0' <= c <= '9':
    print("Caractère numérique")
else:
    print("symbole")
