import numpy as np

a = np.array([1,2,3, -2, 6, -10])
print(a.mean()) # moyenne
print(a.std()) # ecart type
print(a.var()) # variance
print(a.min()) # minimum
print(a.max()) # maximum
print(a.sum()) # somme
print(a.prod()) # produit
print(a.cumsum()) # somme cumulee

print(a[2:4]) # selection de 2 a 4
print(a[2:]) # selection de 2 a la fin
print(a[:4]) # selection de debut a 4
print(a[::-1]) # selection inversee
print(a[2:4:2]) # selection de 2 a 4 avec pas de 2

print(a[a>5]) # selection des valeurs superieur a 5
a[2] = 100 # modification de la valeur a l'index 2
a[a<0] = 0 # modification des valeurs inferieur a 0 par 0



