from .pokedex import verifyType, verifyNumber, MAXNUMBER, TYPES


class Pokemon:
    """Classe que representa um Pokémon."""
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
    """Classe que representa uma pokedex."""
    def __init__(self):
        self.pokemons = {}
    
    def register(self, pokemon):
        """
        Funcionalidade de registrar um Pokémon na pokedex.

        recebe um objeto pokemon que recebe os parametros name, type e number
        type sendo um tipo String de um dos tipos definidos em types do modulo
        pokedex
        """
        if pokemon.number in self.pokemons:
            raise ValueError(f"Pokemon de número {pokemon.number} ja cadastrado")
        else:
            self.pokemons[pokemon.number] = pokemon
            print(f"{pokemon.name} cadastrado com sucesso!")
    
    def search(self, number):
        """
        Funcionalidade para buscar um Pokémon na pokedex pelo numero

        recebe um inteiro que representa o numero do Pokémon.
        retorna um objeto pokemon
        """
        return self.pokemons.get(number, "Pokémon não encontrado")
    
    def update(self, number, name=None, type=None):
        """
        Funcionalidade para atualizar um Pokémon na pokedex pelo numero
        
        recebe parametros number (número do pokemon a ser atualizado),
        dados name (nome do pokemon a ser atualizado) e type (tipo do pokemon a ser atualizado)
        retorna mensagem de sucesso, caso operação seja bem sucedida.
        retorna mensagem de erro, caso operação falhe
        """
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
        """
        Deleta um Pokémon da pokedex pelo numero

        recebe um inteiro que representa o numero do Pokémon
        """
        if number in self.pokemons:
            del self.pokemons[number]
            print(f"Pokémon #{number} removido!")
        else:
            print("Pokémon não encontrado!")

    def getAll(self):
        """Imprime todos os Pokémon registrados na pokedex"""
        for p in sorted(self.pokemons.values(), key=lambda x: x.number):
            print(p)

