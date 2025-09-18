# app/cinema/bar.py

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    # Os testes criam uma instância e chamam como método de instância:
    #   cb = CinemaBar()
    #   cb.sell_product(customer=customer, product=customer.food)
    def sell_product(self, customer: 'Customer', product: str) -> None:
        # Saída EXATA exigida:
        # "Cinema bar sold Sprite to Alice.\n"
        print(f'Cinema bar sold {product} to {customer.name}.')
