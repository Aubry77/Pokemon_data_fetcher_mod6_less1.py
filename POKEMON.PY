import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
data = response.json()

name = data['name']
abilities = [ability['ability']['name'] for ability in data['abilities']]

print(f"Name: {name}")
print("Abilities:", abilities)
