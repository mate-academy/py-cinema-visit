# app/cinema/bar.py

class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        print(f"Cinema bar sold {product} to {customer.name}.")
