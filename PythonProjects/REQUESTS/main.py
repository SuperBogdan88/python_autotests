import requests


response=requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                       json={"name": "generate",
                             "photo": "generate"
                             },
                       headers= {
                                 'Content-Type': 'application/json',
                                 'trainer_token': '357d1020428900307d5963ba048743b6'
                                },
                       timeout=3
                       )

print(response.text)

response=requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
                       json={"pokemon_id": "20212",
                             "name": "generate",
                             "photo": "generate"
                             },
                       headers= {
                                 'Content-Type': 'application/json',
                                 'trainer_token': '357d1020428900307d5963ba048743b6'
                                },
                       timeout=3
                       )

print(response.text)

response=requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                       json={"pokemon_id": "20218"},
                       headers= {
                                 'Content-Type': 'application/json',
                                 'trainer_token': '357d1020428900307d5963ba048743b6'
                                },
                       timeout=3
                       )

print(response.text)




