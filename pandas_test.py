import pandas as pd

df = pd.read_excel('tableur_test.xlsx', sheet_name='contact_drae')

print(df.head(4)) # affiche les 4 premieres lignes
print(df.tail(4)) # affiche les 4 dernieres lignes