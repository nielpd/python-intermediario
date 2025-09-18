from .pokedex import verifyType, verifyNumber, MAXNUMBER, TYPES


class Pokemon:
    def __init__(self, name, type, number):

        if not verifyNumber(number):
            raise ValueError(f"Pokemon de número inválido deve estar entre 1 e {MAXNUMBER}")
        if not verifyType(type):
            raise ValueError(f"Tipo inválido! Deve estar entre {TYPES}")
        
        self.name = name
        self.type = type
        self.number = number

    def __str__(self):
        return f"#{self.number} {self.name} ({self.type})"
    
class Pokedex:
    def __init__(self):
        self.pokemons = {}
    
    def register(self, pokemon):
        if pokemon.number in self.pokemons:
            raise ValueError(f"Pokemon de número {pokemon.number} ja cadastrado")
        else:
            self.pokemons[pokemon.number] = pokemon
            print(f"{pokemon.name} cadastrado com sucesso!")
    
    def search(self, number):
        return self.pokemons.get(number, "Pokémon não encontrado")
    
    def update(self, number, name=None, type=None):
        if number not in self.pokemons:
            print("Pokémon não encontrado!")
            return
        if name:
            self.pokemons[number].name = name
        if type:
            if verifyType(type):
                self.pokemons[number].type = type
            else:
                print(f"Tipo inválido! Deve estar entre {TYPES}")
        print(f"Pokémon #{number} atualizado!")

    def delete(self, number):
        if number in self.pokemons:
            del self.pokemons[number]
            print(f"Pokémon #{number} removido!")
        else:
            print("Pokémon não encontrado!")

    def getAll(self):
        for p in sorted(self.pokemons.values(), key=lambda x: x.number):
            print(p)

