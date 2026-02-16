from app.people.customer import Customer


class CinemaBar:
    def sell_product(self, customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")

    def multiple_sales(self, customers: list[Customer]) -> None:
        for customer in customers:
            self.sell_product(customer, customer.food)
