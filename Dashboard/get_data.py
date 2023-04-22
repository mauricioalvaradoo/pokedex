import pandas as pd
import requests
import json

url  = 'https://mauricioalvaradoo.github.io/pokemon_api/Data/pokemons.json'
file = requests.get(url).json()

# print(json.dumps(file, indent = 3, ensure_ascii=False)[:1203])

poks  = [] #####
names = [] #####
gens  = [] #####
types = []
imgs  = [] #####
eggs  = []
stats = []

for k, v in file.items():   
    for key, val in v.items():
        poks.append(key)
        names.append(val['Name'])
        gens.append(val['Generation'])
        types.append(val['Type'])
        imgs.append(val['Image'])
        eggs.append(val['Egg Group'])
        stats.append(val['Stats'])

df_poks  = pd.DataFrame({'No': poks, 'Nombre': names, 'Generación': gens, 'Imagen': imgs}).set_index('No')
df_types = pd.concat([pd.DataFrame({'No': poks, 'Nombre': names}), pd.get_dummies(pd.DataFrame(types).explode(0)[0]).groupby(level=0).sum()], axis=1).set_index('No')
df_eggs  = pd.concat([pd.DataFrame({'No': poks, 'Nombre': names}), pd.get_dummies(pd.DataFrame(eggs) .explode(0)[0]).groupby(level=0).sum()], axis=1).set_index('No')
df_stats = pd.DataFrame(stats)

df_poks.to_excel('poks.xlsx') 
df_types.to_excel('types.xlsx') 
df_eggs.to_excel('eggs.xlsx') 
df_stats.to_excel('stats.xlsx') 



