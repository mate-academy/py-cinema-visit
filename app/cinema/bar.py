from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: 'Customer') -> None:
        # Ajuste a mensagem se seus testes exigirem um texto específico
        print(f'{customer.name} buys {product} in the cinema bar')
