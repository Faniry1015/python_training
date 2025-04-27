import pandas as pd

df = pd.read_excel('tableur_test.xlsx', sheet_name='contact_drae')

print(df.head(4)) # affiche les 4 premieres lignes
print(df.tail(4)) # affiche les 4 dernieres lignes

print(df.shape) # affiche le nombre de lignes et de colonnes

print(df.columns) # affiche les noms des colonnes

print(df.dtypes) # affiche le type de chaque colonne

print(df['Mail']) # affiche la colonne nom
col = ['Fonction', 'Mail']
print(df[col]) # affiche les colonnes Fonciton et Mail

print(df.loc[0]) # affiche la ligne 0
print(df.loc[[0, 2, 4]]) # affiche les lignes 0, 2 et 4

df['Mail'] = df['Mail'].str.upper() # met en majuscule la colonne Mail

df['test'] = 100 # ajoute une colonne test avec la valeur 100
df.drop(columns=['test']) # supprime la colonne test

df.rename(columns={'N° Téléphone': 'phone'}) # renomme la colonne Mail en mail
print(df.head(4))

df['test'].astype(int) # change le type de la colonne test en int

df.sort_values('Mail', ascending=False) # trie la colonne Mail par ordre decroissant

print(df.iloc[0, 2]) # affiche la valeur de la ligne 0 et de la colonne 2
print(df.iloc[0:2, 1:2]) # affiche les lignes 0 et 1 et les colonnes 1 et 2

#iloc en fonction index ; loc en fonction nom de colonne
df.loc[df['test'] == 100, :] # affiche toutes les lignes ou la colonne test vaut 100

df2 = pd.read_excel('data_purpa.xlsx', sheet_name='mandoto')
print(df2.dtypes)

print(df2.groupby('Commune').mean(numeric_only=True)['Âge']) # moyenne des ages par commune

print(df2.groupby(['Commune', 'Sexe']).count()['Noms']) # nombre de personnes par commune et sexe

print(df2.groupby('Commune').agg({'Noms': 'count', 'Âge': 'mean', 'N°CIN': 'sum'}))  # moyenne des ages par commune et somme des cin


