from app.people.customer import Customer


class CinemaBar:
    # - `bar.py` - inside this module create `CinemaBar`
    # class that describes work of cinema bar.
    # This class should have only one static method `sell_product`,
    # that takes `product` - name of the product that customer wants
    # and `customer` - `Customer` instance, that means customer.
    # The `sell_product` method sells a product
    # to the customer and displays which product was sold and to whom.
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
