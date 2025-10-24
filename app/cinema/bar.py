from .hall import Customer


class CinemaBar:
    """Descreve o funcionamento do cinema bar."""

    @staticmethod
    def sell_product(product: str, customer: Customer):
        """Vende um produto ao cliente e exibe a transação."""
        print(f"Cinema bar sold {product} to {customer.name}.")
