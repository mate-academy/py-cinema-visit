class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer) -> None:
        print(f'Cinema bar sold {customer.food} to {customer.name}.')
