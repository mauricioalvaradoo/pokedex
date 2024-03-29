# API-Pokedex
El despliegue se realizó mediante Github Pages, con la finalidad de evitar el uso de softwares de pago. El archivo 'json' que contiene los datos de toda la API se encuentra en una página web plana, disponible [aquí](https://mauricioalvaradoo.github.io/pokedex/Data/pokemons.json).


## Estructura
Es la siguiente:

```
{
   "Generation 1": {
      "1": {
         "Name": "Bulbasaur",
         "Generation": "Generation 1",
         "Height": "0.7 m (2′04″)",
         "Weight": "6.9 kg (15.2 lbs)",
         "Type": [
            "Grass",
            "Poison"
         ],
         "Image": "https://img.pokemondb.net/artwork/large/bulbasaur.jpg",
         "Egg Group": [
            "Grass",
            "Monster"
         ],
         "Stats": {
            "HP": 45,
            "Attack": 49,
            "Defense": 49,
            "Sp. Atk": 65,
            "Sp. Def": 65,
            "Speed": 45,
            "Total": 318
         },
         "Evolution": [
            "Bulbasaur",
            "Ivysaur",
            "Venusaur"
         ]
      },
      "2": {
         "Name": "Ivysaur",
         "Generation": "Generation 1",
         "Height": "1.0 m (3′03″)",
         "Weight": "13.0 kg (28.7 lbs)",
         "Type": [
            "Grass",
            "Poison"
         ],
         "Image": "https://img.pokemondb.net/artwork/large/ivysaur.jpg",
         "Egg Group": [
            "Grass",
            "Monster"
         ],
         "Stats": {
            "HP": 60,
            "Attack": 62,
            "Defense": 63,
            "Sp. Atk": 80,
            "Sp. Def": 80,
            "Speed": 60,
            "Total": 405
         },
         "Evolution": [
            "Bulbasaur",
            "Ivysaur",
            "Venusaur"
         ]
      }
    }
 }
```
## Acceso
Mediante el código de Python disponible [aquí](https://github.com/mauricioalvaradoo/pokedex/blob/master/get_data_api.py) se puede acceder a la información publicada en Github Pages.
