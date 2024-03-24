import requests
Host = "https://api.pokemonbattle.me/v2"
Trainer_ID = "224"
Trainer_token = "58d888733ce45b57de2789ceffd93e6a"
HEADERS = {"Content-Type" :"application/json",
           "trainer_token" :Trainer_token  }

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url= f'{Host}/pokemons', headers = HEADERS, json = body)

print(response.text)

POKEMON_ID = response.json()['id']

body = {
    "pokemon_id": POKEMON_ID,
    "name": "generate",
}

response = requests.patch(url= f'{Host}/pokemons', headers = HEADERS, json = body)

print(response.text)


body = {
    "pokemon_id": POKEMON_ID
}

response = requests.post(url= f'{Host}/trainers/add_pokeball', headers = HEADERS, json = body)

print(response.text)