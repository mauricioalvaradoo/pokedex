### Creación de Poke API
import utils
import numpy as np
import pickle
from collections import OrderedDict


# Obtención: Url de Pokemons ==================================================
urls = utils.get_urls('https://pokemondb.net/pokedex/all')
urls = [f'https://pokemondb.net{i}' for i in urls]
urls = list(OrderedDict.fromkeys(urls))



# Obtención: Datos de cada Pokemon ============================================
list_name, list_generation, list_height, list_weight, list_type, \
    list_image_url, list_kind, list_stats, list_evolution \
        = utils.get_information(urls)



# Generando código de Pokemon =================================================
list_id = np.linspace(1, len(list_name), len(list_name))\
    .astype('int64').astype('str').tolist()



# Guardado ====================================================================
with open('Data/list_id.pkl', 'wb') as f:
    pickle.dump(list_id, f)
with open('Data/list_name.pkl', 'wb') as f:
    pickle.dump(list_name, f)
with open('Data/list_generation.pkl', 'wb') as f:
    pickle.dump(list_generation, f)
with open('Data/list_height.pkl', 'wb') as f:
    pickle.dump(list_height, f)
with open('Data/list_weight.pkl', 'wb') as f:
    pickle.dump(list_weight, f)
with open('Data/list_type.pkl', 'wb') as f:
    pickle.dump(list_type, f)
with open('Data/list_image_url.pkl', 'wb') as f:
    pickle.dump(list_image_url, f)
with open('Data/list_kind.pkl', 'wb') as f:
    pickle.dump(list_kind, f)
with open('Data/list_stats.pkl', 'wb') as f:
    pickle.dump(list_stats, f)
with open('Data/list_evolution.pkl', 'wb') as f:
    pickle.dump(list_evolution, f)

