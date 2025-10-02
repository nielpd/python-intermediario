"""Módulo `layout` — funcionalidades de layout do rich.

Fornece funções que exibem o texto em diferentes arranjos de layout.
Cada função aceita (texto_or_path: str, isArquivo: bool) e imprime no console
usando recursos do rich.
"""
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
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


def full_layout(text_or_path: str, isArquivo: bool) -> None:
    """Mostra o texto ocupando várias regiões do layout.

    A função cria um layout com header/body/footer e coloca o texto no body
    dentro de um Panel.
    """
    content = _read_text(text_or_path, isArquivo)
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3),
    )
    layout["header"].update(Panel(Text("Personalizador - layout.full_layout", style="bold")))
    layout["body"].split_row(Layout(name="left"), Layout(name="center", ratio=2), Layout(name="right"))
    layout["center"].update(Panel(Text(content)))
    layout["footer"].update(Panel(Text("Fim do layout")))
    console.print(layout)


def side_by_side(text_or_path: str, isArquivo: bool) -> None:
    """Mostra o texto em duas colunas lado a lado (painel esquerdo/direito).

    Ideal para comparar duas partes do conteúdo ou apenas variar a apresentação.
    """
    content = _read_text(text_or_path, isArquivo)
    left = Panel(Text(content[: max(1, len(content) // 2)]), title="Esquerda")
    right = Panel(Text(content[max(1, len(content) // 2):]), title="Direita")
    layout = Layout()
    layout.split_row(Layout(left), Layout(right))
    console.print(layout)
