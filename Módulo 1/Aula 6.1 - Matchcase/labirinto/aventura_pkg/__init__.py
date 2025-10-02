"""Pacote aventura_pkg — contém módulos do jogo Aventura no Labirinto."""

from .labirinto import criar_labirinto, imprimir_labirinto
from .jogador import iniciar_jogador, mover, pontuar
from .utils import imprime_instrucoes, menu_principal, animacao_vitoria

__all__ = [
    "criar_labirinto", "imprimir_labirinto",
    "iniciar_jogador", "mover", "pontuar",
    "imprime_instrucoes", "menu_principal", "animacao_vitoria"
]
