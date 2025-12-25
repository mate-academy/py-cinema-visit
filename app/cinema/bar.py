from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    """Class that describes work of cinema bar."""

    @staticmethod
    def sell_product(customer: "Customer", product: str) -> None:
        """
        Sells a product to the customer and displays
        which product was sold and to whom.

        Args:
            customer: Customer instance
            product: name of the product that customer wants
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
