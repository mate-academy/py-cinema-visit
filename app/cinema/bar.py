from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")

# cb = CinemaBar()
# customer = Customer("Bob", "popcorn")
# cb.sell_product(customer=customer.name, product=customer.food)

# cb = CinemaBar()
# customer = Customer("Bob", "popcorn")
# cb.sell_product(customer=customer, product=customer.food)
# Cinema bar sold popcorn to Bob.

# class Customer:
#     def __init__(self,  customer: str, food: str):
#         self.food = food
#         self.customer = customer
