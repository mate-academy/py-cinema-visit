class CinemaBar:
    @staticmethod
    def sell_product(costumer: dict, product: str) -> None:
        print(f"Cinema bar sold {product} to {costumer['name']}")