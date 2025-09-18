from .pokedex import verifyType, verifyNumber, MAXNUMBER, TYPES
from typing import Optional, Union


class Pokemon:
    """Representa um Pokémon com nome, tipo e número.

    Attributes:
        name (str): Nome do Pokémon.
        type (str): Tipo do Pokémon (deve estar entre os tipos válidos em TYPES).
        number (int): Número do Pokémon (deve estar entre 1 e MAXNUMBER).
    """

    def __init__(self, name: str, type: str, number: int):
        """
        Inicializa um Pokémon.

        Args:
            name (str): Nome do Pokémon.
            type (str): Tipo do Pokémon.
            number (int): Número do Pokémon.

        Raises:
            ValueError: Se o número ou tipo forem inválidos.
        """
        if not verifyNumber(number):
            raise ValueError(f"Pokemon de número inválido deve estar entre 1 e {MAXNUMBER}")
        if not verifyType(type):
            raise ValueError(f"Tipo inválido! Deve estar entre {TYPES}")

        self.name = name
        self.type = type
        self.number = number

    def __str__(self) -> str:
        """Retorna uma representação amigável do Pokémon."""
        return f"#{self.number} {self.name} ({self.type})"


class Pokedex:
    """Representa uma Pokedex, que registra e gerencia Pokémon.

    Attributes:
        pokemons (dict[int, Pokemon]): Dicionário que mapeia número do Pokémon para o objeto Pokémon.
    """

    def __init__(self):
        """Inicializa a Pokedex vazia."""
        self.pokemons: dict[int, Pokemon] = {}

    def register(self, pokemon: Pokemon) -> None:
        """Registra um Pokémon na Pokedex.

        Args:
            pokemon (Pokemon): Objeto Pokémon a ser registrado.

        Raises:
            ValueError: Se o Pokémon já estiver registrado.
        """
        if pokemon.number in self.pokemons:
            raise ValueError(f"Pokemon de número {pokemon.number} já cadastrado")
        self.pokemons[pokemon.number] = pokemon
        print(f"{pokemon.name} cadastrado com sucesso!")

    def search(self, number: int) -> Union[Pokemon, str]:
        """Busca um Pokémon pelo número.

        Args:
            number (int): Número do Pokémon.

        Returns:
            Pokemon | str: Objeto Pokémon se encontrado, ou mensagem de erro caso não exista.
        """
        return self.pokemons.get(number, "Pokémon não encontrado")

    def update(self, number: int, name: Optional[str] = None, type: Optional[str] = None) -> None:
        """Atualiza as informações de um Pokémon pelo número.

        Args:
            number (int): Número do Pokémon a ser atualizado.
            name (str, optional): Novo nome do Pokémon. Defaults to None.
            type (str, optional): Novo tipo do Pokémon. Defaults to None.

        Prints:
            Mensagem de sucesso ou erro dependendo do resultado da atualização.
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

    def delete(self, number: int) -> None:
        """Deleta um Pokémon pelo número.

        Args:
            number (int): Número do Pokémon a ser removido.

        Prints:
            Mensagem de sucesso ou erro dependendo se o Pokémon existia ou não.
        """
        if number in self.pokemons:
            del self.pokemons[number]
            print(f"Pokémon #{number} removido!")
        else:
            print("Pokémon não encontrado!")

    def getAll(self) -> None:
        """Imprime todos os Pokémon registrados na Pokedex, ordenados pelo número."""
        for p in sorted(self.pokemons.values(), key=lambda x: x.number):
            print(p)
