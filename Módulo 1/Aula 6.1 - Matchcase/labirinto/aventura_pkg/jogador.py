"""Módulo jogador — controle de movimento e pontuação do jogador."""
from pynput import keyboard

def iniciar_jogador():
    """Inicializa a posição e pontuação do jogador."""
    return {"pos": (0, 0), "pontos": 0}

def mover(pos_atual, tecla):
    """Atualiza a posição do jogador baseado na tecla pressionada."""
    x, y = pos_atual
    match tecla:
        case "w":
            x = max(0, x - 1)
        case "s":
            x = x + 1
        case "a":
            y = max(0, y - 1)
        case "d":
            y = y + 1
    return (x, y)

def pontuar(jogador):
    """Incrementa pontos do jogador ao mover ou coletar itens."""
    jogador["pontos"] += 1
