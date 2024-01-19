# app/cinema/bar.py
from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> str:
        result = f"Cinema bar sold {product} to {customer.name}."
        print(result)
        return result
