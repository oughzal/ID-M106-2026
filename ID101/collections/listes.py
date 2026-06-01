L = [1,2,3,4,5]

# accès à un élément
print(L[0]) # affiche 1
L[3] = L[1] + L[2] # L[3] devient 5
print(L) # affiche [1, 2, 3, 5, 5]
print(L[-1]) #

# parcours d'une liste
for i in range(len(L)): # Length de la liste
    print(L[i])

for e in L: # parcours direct des éléments de la liste
    print(e)

# ajout d'éléments
L.append(6) # ajoute 6 à la fin de la liste
# insérer un élément à une position donnée
L.insert(2, 10) # insère 10 à l'indice 2

# suppression par position
L.pop(3) # supprime l'élément à l'indice 3
del L # supprime la liste entière

# suppression par valeur
L = [1, 2, 10, 4,10, 5, 6, 10]
L.remove(10) # supprime la première occurrence de 10 dans la liste
for i in range(L.count(10)): # supprime toutes les occurrences de 10
    L.remove(10)

# trouver la position d'un élément
L = [1, 2, 10, 4, 5, 6]
print(L.index(10)) # affiche 2

# trier une liste
L.sort() # trie la liste L
L.sort(reverse=True) # trie la liste L dans l'ordre décroissant

# reverser une liste
L.reverse() # inverse l'ordre des éléments de la liste L

L2 = sorted(L) # retourne une nouvelle liste triée
l3 = reversed(L) # retourne un itérateur pour parcourir la liste à l'envers

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2 # concaténation de listes
L4 = L1 * 3 # répète la liste L1 trois fois
print("*" * 20)

if 10 in L: # vérifie si 10 est dans la liste L
    print("10 est dans la liste")
else:
    print("10 n'est pas dans la liste")