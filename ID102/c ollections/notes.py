ages = [20,30,14,50,40]
print("min :", min(ages))
print("max :", max(ages))
print("moyenne :", sum(ages)/len(ages))
majeurs =[]
for age in ages:
    if age >= 18:
        majeurs.append(age)
print("majeurs :", majeurs)

ages.remove(16)