import requests

token = '4e50fcf07872d063e2389944cd23b027'
Url = 'https://pokemonbattle.me:9104/'

answer = requests.post(f'{Url}pokemons' , headers = {"trainer_token": token}, json =
{
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"

} )
print(answer.text)

response = requests.put(f'{Url}pokemons' , headers = {"trainer_token": token}, json={
    "pokemon_id": "13827",
    "name": "Саня",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response.text)


add_pocketball = requests.post(f'{Url}trainers/add_pokeball', headers = {"trainer_token": token}, json={
        "pokemon_id": "13827"
})

print(add_pocketball.text)