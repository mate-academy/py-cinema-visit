from app.people.customer import Customer


class CinemaBar:
    """
    Manages product sales operations within the cinema.
    """
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        """
        Print the sales message, linking the product to the customer.

        Args:
            customer (Customer): cinema customer who buys a product.
            product (str): item that the customer buys.

        Returns:
            None

        Print:
            The transaction between the cinema and the customer.
        """
        print(f"Cinema bar sold {product} to {customer}.")
