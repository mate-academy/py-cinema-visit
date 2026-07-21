# via TYPE_CHECKING to avoid circular dependencies,
# if Customer wants someday will want to import Bar.
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    # @staticmethod means the method doesn't require a class object (self).
    @staticmethod
    def sell_product(
        product: str,
        customer: "Customer"
    ) -> None:
        # Use the data from the customer object (its name),
        # to form a message.
        print(f"Cinema bar sold {product} to {customer.name}.")
