from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """
        Sells a product to a customer.

        Parameters:
        product (str): The name of the product to be sold.
        customer (Customer): The customer who is buying the product.
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
