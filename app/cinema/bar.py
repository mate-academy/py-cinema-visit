from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")


if __name__ == "__main__":
    cinema_bar = CinemaBar()
    customer = Customer("Bob", "popcorn")
    cinema_bar.sell_product(customer=customer, product=customer.food)
    # Cinema bar sold popcorn to Bob.
