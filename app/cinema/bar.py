from __future__ import annotations


from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == "__main__":
    visitor = Customer("Alice", "Sprite")
    CinemaBar.sell_product(visitor, visitor.food)
