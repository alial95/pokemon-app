import urllib.request as req
import json
import csv
from poke_class import Pokemon
pokemon_url = f"https://pokeapi.co/api/v2/pokemon-species/?offset=0&limit=151"
# items_url = "https://pokeapi.co/api/v2/item"
count = 1
def read_url(url):
    urls = []
    request = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    origin = req.urlopen(request)
    data = json.load(origin)
    results = data['results']
    for url in results:
        urls.append(url['url'])
    return urls
def get_pokemon_info(url_list):
    pokemon = []
    for url in url_list:
        request = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        origin = req.urlopen(request)
        data = json.load(origin)
        description = data["flavor_text_entries"][0]['flavor_text']
        colour = data['color']['name']
        pokedex = data['id']
        pokemon_data = Pokemon(data['name'], description, colour, pokedex)
        pokemon.append(pokemon_data)
    return pokemon




# items_bytes = read_url(items_url)
poke_urls = read_url(pokemon_url)
pokemon = get_pokemon_info(poke_urls)
print(pokemon[50].description)
# request = req.Request(poke_urls[0], headers={'User-Agent': 'Mozilla/5.0'})
# origin = req.urlopen(request)
# data = json.load(origin)
# description = data["flavor_text_entries"][0]['flavor_text']
# def clean_description(description):

# print(description)
# poke_1 = poke_bytes['results']

# items_1 = items_bytes['results']
# print(items_1)
# items = []
# pokemon = []
# for value in poke_1:
#     pokemon.append(value['name'])
# for value in items_1:
#     items.append(value['name'])
# poke_balls = []
# for item in items:
#     if 'ball' in item:
#         poke_balls.append(item)
# print(poke_balls)
# print(pokemon[:25])
# with open('pokemon.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=' ')
#     for row in pokemon:
#         writer.writerows(row)


# def get_favourite_pokemon():
#     fav_poke = input('Please enter your favourite pokemon: ')