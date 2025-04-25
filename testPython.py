prenoms = ["Pierre", "Jean", "Monique"]
age = [30, 35, 60]
dico = {k:v for k,v in enumerate(prenoms)}
dico_1 = {k:v for k,v in zip(prenoms, age) if v > 32 } #if ajoute une condition

print(dico)
print(dico_1)