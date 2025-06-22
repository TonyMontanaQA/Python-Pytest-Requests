import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '657d4cf3292e0be1f3e0719e7c05ae5c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_post_pokemon = {
    "name": "generate",
    "photo_id": -1
}
body_put_rename = {
    "pokemon_id": "340861",
    "name": "Masha",
    "photo_id": 2
}
body_post_pokeball = {
    "pokemon_id": "340920"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_post_pokemon)
print(response.status_code)

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put_rename)
print(response_rename.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_post_pokeball)
print(response_pokeball.status_code)'''