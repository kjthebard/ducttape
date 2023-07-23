import duckdb
import requests
import pprint as pp
import json


url = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 1281}

# Gets data
response = requests.get(url, params=params)

if response.status_code != 200: 
    print(response.text)
else:
    data = response.json()

json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("all_pokemon.json", "w") as outfile:
    outfile.write(json_object)