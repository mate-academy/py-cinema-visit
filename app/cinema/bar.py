from app.people.customer import Customer
class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer) -> None:
        print(f"Cinema bar sold {customer.food} to {customer.name}.")
