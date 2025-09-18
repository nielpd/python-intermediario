MAXNUMBER = 150
TYPES = ('Normal', 'Fogo', 'Água', 'Planta', 'Elétrico', 'Gelo', 
         'Lutador', 'Venenoso', 'Terra', 'Voador', 'Psíquico', 
         'Inseto', 'Pedra', 'Fantasma', 'Dragão', 
         'Noturno', 'Metálico', 'Fada')

def verifyType(type): 
    return type in TYPES

def verifyNumber(n):
    return 1 <= n <= MAXNUMBER