from pokeregister import Pokedex, Pokemon

pokedex = Pokedex()

print("Documentação de: pokeregister.Pokedex().register().__doc__\n" 
      + pokedex.register.__doc__)

print("Documentação de: pokeregister.Pokedex().search().__doc__\n" 
      + pokedex.search.__doc__)

print("Documentação de: pokeregister.Pokedex().update().__doc__\n" 
      + pokedex.update.__doc__)

print("Documentação de: pokeregister.Pokedex().delete().__doc__\n" 
      + pokedex.delete.__doc__)

print("Documentação de: pokeregister.Pokedex().getAll().__doc__\n" 
      + pokedex.getAll.__doc__)