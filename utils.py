from typing import Optional


def print_line(width: int = 40) -> None:
    print('-' * width)


def ask_int(prompt: str) -> Optional[int]:
    """Lê um inteiro do input; retorna None se inválido."""
    try:
        return int(input(prompt))
    except ValueError:
        return None
