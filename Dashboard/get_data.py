import pandas as pd
import requests
import json

url  = 'https://mauricioalvaradoo.github.io/pokemon_api/Data/pokemons.json'
file = requests.get(url).json()

# print(json.dumps(file, indent = 3, ensure_ascii=False)[:1450])

poks  = []
names = []
gens  = []
heigs = []
weigs = []
types = []
imgs  = []
eggs  = []
stats = []
evols = []

for k, v in file.items():   
    for key, val in v.items():
        poks. append(key)
        names.append(val['Name'])
        gens. append(val['Generation'])
        heigs.append(val['Height'])
        weigs.append(val['Weight'])
        types.append(val['Type'])
        imgs. append(val['Image'])
        eggs. append(val['Egg Group'])
        stats.append(val['Stats'])
        evols.append(val['Evolution'])

df_poks  = pd.DataFrame({'No': poks, 'Nombre': names, 'Altura': heigs, 'Peso': weigs, 'Generación': gens, 'Imagen': imgs}).set_index('No')
df_types = pd.concat([pd.DataFrame({'No': poks, 'Nombre': names}), pd.get_dummies(pd.DataFrame(types).explode(0)[0]).groupby(level=0).sum()], axis=1).set_index('No')
df_eggs  = pd.concat([pd.DataFrame({'No': poks, 'Nombre': names}), pd.get_dummies(pd.DataFrame(eggs) .explode(0)[0]).groupby(level=0).sum()], axis=1).set_index('No')
df_stats = pd.concat([pd.DataFrame({'No': poks, 'Nombre': names}), pd.DataFrame(stats)], axis=1).set_index('No')
df_evols = pd.concat([pd.DataFrame({'No': poks, 'Nombre': names}), pd.DataFrame(evols)], axis=1).set_index('No')

# Saving
with pd.ExcelWriter('Dashboard/data.xlsx') as writer:
    df_poks. to_excel(writer, sheet_name='poks' )
    df_types.to_excel(writer, sheet_name='types')
    df_eggs. to_excel(writer, sheet_name='eggs' )
    df_stats.to_excel(writer, sheet_name='stats')
    df_evols.to_excel(writer, sheet_name='evols')

