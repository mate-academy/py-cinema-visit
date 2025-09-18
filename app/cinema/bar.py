class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        # product first, customer second per spec
        print(f"Cinema bar sold {product} to {customer.name}.")

# preserve module‐level alias
sell_product = CinemaBar.sell_product
