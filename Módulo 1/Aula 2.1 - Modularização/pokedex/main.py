from pokeregister import Pokedex, Pokemon

pokedex = Pokedex()

pokemon1 = Pokemon(number=1, name="Bulbasaur", type="Planta")
pokemon2 = Pokemon(number=2, name="Ivysaur", type="Planta")
pokemon3 = Pokemon(number=3, name="Venusaur", type="Planta")
pokemon4 = Pokemon(number=4, name="Charmander", type="Fogo")
pokemon5 = Pokemon(number=5, name="Charmeleon", type="Fogo")
pokemon6 = Pokemon(number=6, name="Charizard", type="Fogo")
pokemon7 = Pokemon(number=7, name="Squirtle", type="Água")
pokemon8 = Pokemon(number=8, name="Wartortle", type="Água")
pokemon9 = Pokemon(number=9, name="Blastoise", type="Água")

pokedex.register(pokemon1)
pokedex.register(pokemon2)
pokedex.register(pokemon3)
pokedex.register(pokemon4)
pokedex.register(pokemon5)
pokedex.register(pokemon6)
pokedex.register(pokemon7)
pokedex.register(pokemon8)
pokedex.register(pokemon9)

pokedex.getAll()
