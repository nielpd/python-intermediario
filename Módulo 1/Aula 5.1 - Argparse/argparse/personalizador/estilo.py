"""Módulo `estilo` — funcionalidades de estilo do rich.

Aplica estilos (negrito, itálico, underlines, regras etc.) ao texto recebido.
"""
from rich.console import Console
from rich.rule import Rule
from rich.text import Text

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


def emphasize(text_or_path: str, isArquivo: bool) -> None:
    """Aplica ênfase ao texto (negrito + sublinhado) e imprime entre regras."""
    content = _read_text(text_or_path, isArquivo)
    console.print(Rule(title="Início"))
    console.print(Text(content, style="bold underline"))
    console.print(Rule(title="Fim"))


def colorful_lines(text_or_path: str, isArquivo: bool) -> None:
    """Quebra o texto em linhas e aplica estilos alternados a cada linha."""
    content = _read_text(text_or_path, isArquivo)
    lines = content.splitlines() or [content]
    styles = ["bold red", "italic green", "reverse yellow", "underline blue"]
    for idx, line in enumerate(lines):
        console.print(Text(line, style=styles[idx % len(styles)]))
