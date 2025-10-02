"""Módulo `painel` — funcionalidades de painel do rich.

Fornece funções que exibem o texto dentro de Painéis com estilos diferentes.
"""
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

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


def panel_classic(text_or_path: str, isArquivo: bool) -> None:
    """Exibe o texto dentro de um Panel clássico com borda box.ROUNDED."""
    content = _read_text(text_or_path, isArquivo)
    console.print(Panel(Text(content), title="Painel Clássico", box=box.ROUNDED))


def panel_with_header(text_or_path: str, isArquivo: bool) -> None:
    """Exibe o texto dentro de um painel com cabeçalho e subcabeçalho.

    Mostra também uma pequena instrução no rodapé do painel.
    """
    content = _read_text(text_or_path, isArquivo)
    header = Text("Cabeçalho do Painel", style="bold underline")
    body = Text(content)
    footer = Text("(exibido via personalizador.painel.panel_with_header)")
    panel = Panel(body, title=header, subtitle=footer, box=box.SQUARE)
    console.print(panel)
