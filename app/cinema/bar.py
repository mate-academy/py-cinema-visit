"""
bar.py - inside this module create CinemaBar class that describes work
 of cinema bar. This class should have only one static method sell_product,
 that takes product - name of the product that customer wants and
 customer - Customer instance, that means customer. This method prints
 what product and to whom cinema sold.
cb = CinemaBar()
customer = Customer("Bob", "popcorn")
cb.sell_product(customer=customer, product=customer.food)
    # Cinema bar sold popcorn to Bob.
"""


from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
