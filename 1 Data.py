### CreaciÃ³n de Poke API
# import pandas as pd
# import numpy as np
import utils


# Obtención: Url de Pokemons
urls = utils.get_urls('https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon')
urls = [f'https://pokemon.fandom.com{i}' for i in urls]
urls = urls[0:2]


# Obtención: Datos de Pokemon
list_id, list_name, list_generation, list_type, \
    list_image_url, list_kind = utils.get_information(urls)


