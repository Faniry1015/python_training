nbreVie = 7
mot = ["p","y","t","h","o","n"]
# mot = "python"
trouver = ["*","*","*","*","*","*"]

while nbreVie > 0 :
    letter = input("Entre une lettre : ")
    if letter in mot:
        index = mot.index(letter)
        trouver[index] = letter
        print(trouver)
    else:
        nbreVie -= 1
        print("La lettre ",letter, " n'existe pas dans le mot, il vous reste ", nbreVie, " tentative(s)")
print("Game Over")