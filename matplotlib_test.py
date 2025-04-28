import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('matplot_test.xlsx', sheet_name='meteo')
villes = data['ville']
temp = data['temperature']
prec = data['precipitation']

points = plt.scatter(temp, prec) # affiche les points
plt.show()

batonne = plt.bar(villes, temp) # affiche les barres
plt.xlabel('Ville')
plt.ylabel('Température')
plt.title('Températures par ville')
plt.show()

plt.hist(temp, bins=10, edgecolor='red') # histogramme
plt.show()

plt.pie(temp, labels=villes) # diagramme en secteurs
plt.show()

plt.pie(temp, labels=villes, autopct='%1.1f%%') # diagramme en secteurs avec pourcentage
plt.show()

plt.plot(villes, prec) # affiche la courbe
plt.show()

# Plusieurs graphiques sur une seule fenêtre
plt.figure()
plt.subplot(221) # 2 lignes et 2 colonnes et 1er graphique
plt.plot(villes, prec)
plt.subplot(222) # 2 lignes et 2 colonnes et 2eme graphique
plt.plot(villes, temp)
plt.subplot(223) # 2 lignes et 2 colonnes et 3eme graphique
plt.pie(temp, labels=villes)
plt.subplot(224) # 2 lignes et 2 colonnes et 4eme graphique
plt.hist(temp, bins=10, edgecolor='red')
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.5) # ajuste les marges: top, bottom, left, right, hspace, wspace
plt.show()