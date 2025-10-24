from ..people.customer import Customer


class CinemaBar:
    """
    Descreve o funcionamento do cinema bar, usado para registrar
    a venda de produtos.
    """
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        """
        Metodo estático que registra a venda de um produto para
        um cliente.
        """
        # A mensagem é formatada conforme o exemplo: Cinema bar sold
        # [produto] to [cliente.name].
        print(f"Cinema bar sold {product} to {customer.name}.")
