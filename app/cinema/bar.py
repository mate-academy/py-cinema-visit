from app.people.customer import Customer


class CinemaBar:
    # Classe para o bar do cinema
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        # Imprime que vendeu um produto ao cliente
        print(f"Cinema bar sold {product} to {customer.name}.")
