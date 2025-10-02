"""Módulo utils — funções utilitárias do jogo."""
from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def imprime_instrucoes():
    """Imprime instruções do jogo formatadas."""
    instrucoes = "Use W/A/S/D para se mover. Chegue ao X para vencer!"
    console.print(Panel(instrucoes, title="Instruções"))

def menu_principal():
    """Imprime menu principal."""
    console.print("[1] Instruções\n[2] Jogar\n[3] Sair")

def animacao_vitoria(passos=5):
    """Exemplo de função recursiva para animar vitória."""
    if passos == 0:
        return
    console.print("🎉 Vitória! 🎉" * passos)
    sleep(0.3)
    animacao_vitoria(passos - 1)
