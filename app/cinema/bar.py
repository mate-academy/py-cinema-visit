from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: str) -> str:
        return f"Cinema bar sold {product} to {customer}."


# cb = CinemaBar()
# customer = Customer("Bob", "popcorn")
# print(cb.sell_product(customer=customer.name, product=customer.food))
# # Cinema bar sold popcorn to Bob.