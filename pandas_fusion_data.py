#Fusion de données (données provenant de plusieurs sources)
import pandas as pd

client = pd.read_excel('data_vente.xlsx', sheet_name='client_info')
achat = pd.read_excel('data_vente.xlsx', sheet_name='achat_info')

data = pd.merge(achat, client) # merge les deux tableaux il reconnait directement le client_id comme clé commune

print(data[['client_nom', 'article_num', 'article_nbre']]) 
print(data.groupby('client_nom').sum('article_nbre')['article_num'])

data2 = pd.merge(achat, client, how='inner', on='client_id') #merge par défaut : Jointure interne : Inner ; il y a 'left' et 'right' aussi
print(data2)
