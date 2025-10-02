import argparse
from aventura_pkg import labirinto, jogador, utils
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument("--name", type=str, required=True, help="Nome do jogador")
    parser.add_argument("--color", type=str, default="green", help="Cor do jogador")
    parser.add_argument("--dificuldade", type=int, choices=[5, 7, 10], default=5, help="Tamanho do labirinto")
    parser.add_argument("--disable-sound", action="store_true", help="Desliga sons")
    parser.add_argument("--menu", action="store_true", help="Mostra menu inicial")

    args = parser.parse_args()

    if args.menu:
        utils.menu_principal()
        return

    console.print(f"Bem-vindo(a), [bold {args.color}]{args.name}[/bold {args.color}]!")

    lab = labirinto.criar_labirinto(args.dificuldade)
    labirinto.imprimir_labirinto(lab)

    j = jogador.iniciar_jogador()
    utils.animacao_vitoria(3)

if __name__ == "__main__":
    main()
