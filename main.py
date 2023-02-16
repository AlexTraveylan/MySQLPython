from MySqlService import PokemonService


pService = PokemonService()
pokemons = pService.getAll()

pokemons = pService.getAll()
for pokemon in pokemons:
    print(pokemon)

pService.close()







