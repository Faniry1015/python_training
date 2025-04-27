import pandas as pd

client = pd.read_excel('data_vente.xlsx', sheet_name='client_info')
achat = pd.read_excel('data_vente.xlsx', sheet_name='achat_info')

print(achat.merge(client)) # merge les deux tableaux il reconnait directement le client_id comme clé