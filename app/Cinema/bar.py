# app/cinema/bar.py

class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        print(f"{product} was sold to {customer.name}")
