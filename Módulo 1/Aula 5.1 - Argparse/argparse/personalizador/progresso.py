"""Módulo `progresso` — funcionalidades de progresso do rich.

Contém funções que demonstram barras de progresso e animações simples.
"""
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
from time import sleep

console = Console()


def _read_text(text_or_path: str, isArquivo: bool) -> str:
    """Lê o conteúdo do arquivo se isArquivo for True, caso contrário retorna a string."""
    if isArquivo:
        try:
            with open(text_or_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Erro ao ler arquivo: {e}"
    return text_or_path


def show_progress(text_or_path: str, isArquivo: bool) -> None:
    """Exibe o texto e simula uma tarefa com barra de progresso.

    A função mostra o conteúdo e uma barra que progride lentamente.
    """
    content = _read_text(text_or_path, isArquivo)
    console.print("Iniciando tarefa...\n")
    console.print(content)
    with Progress(
        TextColumn("{task.description}"),
        BarColumn(),
        TimeElapsedColumn()
    ) as progress:
        task = progress.add_task("Processando", total=100)
        for _ in range(100):
            sleep(0.01)
            progress.update(task, advance=1)


def animated_spinner(text_or_path: str, isArquivo: bool) -> None:
    """Mostra uma animação simples de 'processamento' enquanto exibe o texto."""
    content = _read_text(text_or_path, isArquivo)
    console.print("Iniciando animação...\n")
    console.print(content)
    for i in range(6):
        console.print(f"Passo {i+1}/6", end="\r")
        sleep(0.3)
    console.print()  
