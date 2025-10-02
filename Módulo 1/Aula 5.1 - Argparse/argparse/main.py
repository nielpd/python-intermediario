import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(
        description="Ferramenta de personalização com Rich"
    )

    parser.add_argument(
        "texto",
        type=str,
        help="Texto a ser exibido ou caminho para arquivo"
    )

    parser.add_argument(
        "-a", "--arquivo",
        action="store_true",
        help="Indica que o argumento é o caminho para um arquivo"
    )

    parser.add_argument(
        "-m", "--modulo",
        required=True,
        choices=["layout", "painel", "progresso", "estilo"],
        help="Escolha o módulo a ser utilizado"
    )

    parser.add_argument(
    "-f", "--funcao",
    required=True,
    choices=[
        "full_layout", "side_by_side",
        "panel_classic", "panel_with_header",
        "show_progress", "animated_spinner",
        "emphasize", "colorful_lines"
    ],
    help="Escolha a função do módulo"
    )

    args = parser.parse_args()

    modulos = {
        "layout": layout,
        "painel": painel,
        "progresso": progresso,
        "estilo": estilo
    }

    modulo = modulos[args.modulo]

    funcao = getattr(modulo, args.funcao, None)

    if funcao is None:
        print(f"Função {args.funcao} não encontrada no módulo {args.modulo}.")
        return

    funcao(args.texto, args.arquivo)


if __name__ == "__main__":
    main()
