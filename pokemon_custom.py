import my_requests

def fetch_pokemon_data(pokemon_name):
    """
    Fetches data for a given Pokémon from the Pokémon API.

    Args:
        pokemon_name (str): The name of the Pokémon to fetch data for.

    Returns:
        dict: The data of the Pokémon, or None if an error occurred.
    """
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        return my_requests.get(url)
    except Exception as e:
        print(f"Error fetching data for {pokemon_name}: {e}")
        return None

def calculate_average_weight(pokemon_list):
    """
    Calculates the average weight of a list of Pokémon.

    Args:
        pokemon_list (list): The list of Pokémon data.

    Returns:
        float: The average weight of the Pokémon.
    """
    valid_pokemon = [pokemon for pokemon in pokemon_list if pokemon]
    total_weight = sum(pokemon['weight'] for pokemon in valid_pokemon)
    return total_weight / len(valid_pokemon) if valid_pokemon else 0

pokemon_names = ["pikachu", "bulbasaur", "charmander", "invalid_pokemon"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_data:
    if pokemon:
        name = pokemon['name']
        abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        print(f"Name: {name}, Abilities: {abilities}")

average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight} units")
