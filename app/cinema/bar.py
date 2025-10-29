from app.people.customer import Customer

class CinemaBar:
    """
    Descreve o funcionamento do cinema bar.
    Possui apenas um metodo estático para vender produtos.
    """

    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """
        Vende um produto ao cliente e exibe qual produto foi vendido e para quem.
        """
        print(f"Cinema bar sold {product} to {customer.name}.")
