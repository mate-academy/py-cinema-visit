from __future__ import annotations


class CinemaBar:
    @staticmethod
    def sell_product(customer: "Customer"
                     , product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == "__main__":
    from app.people.customer import Customer
