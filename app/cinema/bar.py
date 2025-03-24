from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: Customer, customer: Customer):
        print(f"Cinema bar sold {product} to {customer.name}.")