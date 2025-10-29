from app.people.customer import Customer


class CinemaBar:
    """
    Represents a cinema bar where products can
    be sold to customers.

    This class is designed to simulate the
    operations of a cinema bar which sells
    products to customers inside a cinema.
    It provides a method to manage the sale
    of products in association with customer
    information.

    """
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """
        Sell a product to a customer. This static method
        is used to simulate the sale of a product
        such as snacks or beverages to a customer in the cinema bar.
        Upon execution, it logs a message indicating the specific
        product sold and the name of the customer it was sold to.

        :param product: The name of the product being sold.
        :type product: str
        :param customer: The customer buying the product.
            Should be an instance of the Customer class.
        :type customer: Customer
        :return: None
        :rtype: None
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
