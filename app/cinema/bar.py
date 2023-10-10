from app.people.cinema_staff import Cleaner


class CinemaBar:
    @staticmethod
    def sell_product(customer: Cleaner, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
