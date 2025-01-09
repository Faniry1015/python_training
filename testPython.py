list_1 = [-1, 2, 6, -10, 50, 100, 4, -20]

classeur1  = {
    "positif": [],
    "negatif": []
}
def trier(classeur, nombres):
    for nombre in nombres :
        if nombre >=0 :
            classeur["positif"].append(nombre) 
        else: 
            classeur["negatif"].append(nombre)
    return classeur

print(trier(classeur1, list_1))