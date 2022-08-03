from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: str):
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == '__main__':
    cb = CinemaBar()
    customer = Customer("Bob", "popcorn")
    print(cb.sell_product(customer=customer, product=customer.food))
