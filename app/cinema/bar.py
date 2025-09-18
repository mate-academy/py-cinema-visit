# app/cinema/bar.py

class CinemaBar:
    @staticmethod
    def sell_product(customer, product):
        print(f"Cinema bar sold {product} to {customer.name}.")

# цей рядок мусить бути поза рівнем класу:
sell_product = CinemaBar.sell_product
