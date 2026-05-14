ages = [22, 25, 30]
print(f"max : {max(ages)}")
print(f"min : {min(ages)}")
print(f"moyenne : {sum(ages)/len(ages)}")

majeurs = []
for age in ages:
    if age >= 18:
        majeurs.append(age)
print(f"majeurs : {majeurs}")
ages.sort()
print(f"ages triés : {ages}")
ages.remove(16)

for age in ages:
    if 20<= age and age <= 50:
        print(f"age : {age}")