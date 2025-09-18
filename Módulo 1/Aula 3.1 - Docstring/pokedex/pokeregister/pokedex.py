MAXNUMBER = 150
TYPES = (
    'Normal', 'Fogo', 'Água', 'Planta', 'Elétrico', 'Gelo',
    'Lutador', 'Venenoso', 'Terra', 'Voador', 'Psíquico',
    'Inseto', 'Pedra', 'Fantasma', 'Dragão',
    'Noturno', 'Metálico', 'Fada'
)


def verifyType(type: str) -> bool:
    """Verifica se o tipo informado é válido.

    Args:
        type (str): Tipo do Pokémon a ser verificado.

    Returns:
        bool: True se o tipo estiver em `TYPES`, False caso contrário.
    """
    return type in TYPES


def verifyNumber(n: int) -> bool:
    """Verifica se o número do Pokémon está dentro do intervalo permitido.

    Args:
        n (int): Número do Pokémon a ser verificado.

    Returns:
        bool: True se o número estiver entre 1 e `MAXNUMBER`, False caso contrário.
    """
    return 1 <= n <= MAXNUMBER
