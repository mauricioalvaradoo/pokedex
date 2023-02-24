import pandas as pd
import numpy as np
import pickle
import json




# Importación =================================================================
with open('Data/list_id.pkl', 'rb') as f:
    list_id = pickle.load(f)
with open('Data/list_name.pkl', 'rb') as f:
    list_name = pickle.load(f)
with open('Data/list_generation.pkl', 'rb') as f:
    list_generation = pickle.load(f)
with open('Data/list_type.pkl', 'rb') as f:
    list_type = pickle.load(f)
with open('Data/list_image_url.pkl', 'rb') as f:
    list_image_url = pickle.load(f)
with open('Data/list_kind.pkl', 'rb') as f:
    list_kind = pickle.load(f)
with open('Data/list_stats.pkl', 'rb') as f:
    list_stats = pickle.load(f)



# Modificaciones a los URL de las imágenes ====================================
# Reducción
list_image_url = [i.split('.png')[0] for i in list_image_url]
list_image_url = [f'{i}.png' for i in list_image_url]

# Reemplazar el único pokemon sin imagen
for i in range(len(list_image_url)):
    if list_image_url[i] == '.png':
        list_image_url[i] = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/973.png'




# Estructura ==================================================================
pokemons_v1 = {}

for i in range(1, len(list_id)+1):
    
    pokemons_v1[i] = {
        'Name': list_name[i-1],
        'Generación': list_generation[i-1],
        'Tipo': list_type[i-1],
        'Imagen': list_image_url[i-1],
        'Egg Group': list_kind[i-1],
        'Stats': list_stats[i-1]
    }



# Reestructurando =============================================================
pokemons_v2 = {}

for key, value in pokemons_v1.items():
    generation = value['Generación']
    
    if generation not in pokemons_v2:
        pokemons_v2[generation] = {}
    
    pokemons_v2[generation][key] = value



# Observar la estructura ======================================================
# Ver los dos primeros pokemons
print(json.dumps(pokemons_v2, indent = 3, ensure_ascii=False)[:1203])




# Exportando la estructura ====================================================
with open('Data/pokemons.pkl', 'wb') as f:
    pickle.dump(pokemons_v2, f)


