from typing import Dict, Optional, Tuple

SNACKS: Dict[str, int] = {
    'Pipoca': 20,
    'Refrigerante': 12,
    'Chocolate': 15,
}


def list_snacks() -> str:
    """Lista formatada dos snacks e seus preços."""
    return '\n'.join([f'{i + 1}. {s} - {p} NIS'for i,
                     (s, p) in enumerate(SNACKS .items())])


def get_snack_price(snack: str) -> Optional[int]:
    """Preço de um snack pelo nome (ou None se inválido)."""
    return SNACKS .get(snack)


def buy_snack(snack: str, qty: int, price: int) -> int:
    """Calcula o custo total do snack escolhido."""
    return qty * price


def get_snack_by_index(idx: int) -> Optional[Tuple[str, int]]:
    """Retorna (nome, preço) do snack pelo índice 1-based; None se inválido."""
    if 1 <= idx <= len(SNACKS):
        name = list(SNACKS .keys())[idx - 1]
        return name, SNACKS[name]
    return None
