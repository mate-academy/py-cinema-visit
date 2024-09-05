from app.people.customer import Customer


class CinemaBar:
    """
    A class representing the cinema bar where customers can buy food.

    Methods:
        sell_product(product: str, customer: Customer) -> None:
            Sells a product to a customer and prints a message indicating
            the transaction.
    """
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """
        Prints a message, that the cinema bar sold a product to the customer.

        Args:
            product (str): The name of the product being sold.
            customer (Customer): The customer buying the product.
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
