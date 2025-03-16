from app.people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print("Cinema bar sold {} to {}.".format(product, customer.name))
