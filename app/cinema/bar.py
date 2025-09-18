from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    """API minimalista conforme os testes."""
    def __init__(self: 'CinemaBar') -> None:
        self.menu: dict[str, int] = {}

    def get_price(self: 'CinemaBar', item: str) -> int | None:
        return self.menu.get(item)

    def buy(self: 'CinemaBar', item: str, qty: int) -> int | None:
        price = self.get_price(item)
        if price is None:
            return None
        return price * max(qty, 0)

    def sell_product(self: 'CinemaBar', customer: 'Customer', product: str) -> None:
        # Saída exata cobrada pelos testes
        print(f'Cinema bar sold {product} to {customer.name}.')
