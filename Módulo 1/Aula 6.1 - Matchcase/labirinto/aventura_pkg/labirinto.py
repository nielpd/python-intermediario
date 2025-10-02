"""Módulo labirinto — funções para criar e imprimir o labirinto."""
import random
from rich.console import Console
from rich.table import Table

console = Console()

def criar_labirinto(tamanho: int = 5):
    """Gera um labirinto aleatório com paredes (#) e espaços livres ( )."""
    labirinto = []
    for _ in range(tamanho):
        linha = [random.choice([" ", "#"]) for _ in range(tamanho)]
        labirinto.append(linha)
    labirinto[0][0] = "J"  # posição inicial do jogador
    labirinto[tamanho-1][tamanho-1] = "X"  # objetivo
    return labirinto

def imprimir_labirinto(labirinto: list):
    """Imprime o labirinto no terminal usando Rich Table."""
    table = Table(show_header=False, box=None)
    for _ in labirinto[0]:
        table.add_column(justify="center")
    for linha in labirinto:
        table.add_row(*linha)
    console.print(table)
