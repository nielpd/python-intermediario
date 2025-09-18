MAXNUMBER = 150
TYPES = ('Normal', 'Fogo', 'Água', 'Planta', 'Elétrico', 'Gelo', 
         'Lutador', 'Venenoso', 'Terra', 'Voador', 'Psíquico', 
         'Inseto', 'Pedra', 'Fantasma', 'Dragão', 
         'Noturno', 'Metálico', 'Fada')

def verifyType(type): 
    """Verifica se o tipo é um dos tipos permitidos.
    
    recebe uma string que representa um dos tipos permitidos.
    retorna um booleano se o tipo é permitido ou nao
    """
    return type in TYPES
  

def verifyNumber(n):
    """
    Verifica se o número do Pokémon é permitido.

    recebe um inteiro que representa o número do Pokémon.
    retorna um booleano se o número é permitido ou nao
    """
    return 1 <= n <= MAXNUMBER