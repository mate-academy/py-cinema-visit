# app/cinema/bar.py
from app.people.customer import Customer

class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        print(f'cinema bar sold {product} to {customer.name}.')

