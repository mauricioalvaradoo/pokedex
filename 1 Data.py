### Creación de Poke API
import utils
import pickle


# Obtención: Url de Pokemons ==================================================
urls = utils.get_urls('https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon')
urls = [f'https://pokemon.fandom.com{i}' for i in urls]


# Obtención: Datos de cada Pokemon ============================================
list_id, list_name, list_generation, list_type, list_image_url, \
    list_kind, list_stats = utils.get_information(urls)


# Guardado ====================================================================
with open('Data/list_id.pkl', 'wb') as f:
    pickle.dump(list_id, f)
with open('Data/list_name.pkl', 'wb') as f:
    pickle.dump(list_name, f)
with open('Data/list_generation.pkl', 'wb') as f:
    pickle.dump(list_generation, f)
with open('Data/list_type.pkl', 'wb') as f:
    pickle.dump(list_type, f)
with open('Data/list_image_url.pkl', 'wb') as f:
    pickle.dump(list_image_url, f)
with open('Data/list_kind.pkl', 'wb') as f:
    pickle.dump(list_kind, f)
with open('Data/list_stats.pkl', 'wb') as f:
    pickle.dump(list_stats, f)

