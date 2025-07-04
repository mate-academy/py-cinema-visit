from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(customer: object | str, product: str) -> None:
        element = Customer("", product)
        if isinstance(customer, Customer):
            print(f"Cinema bar sold {element.food} to {customer.name}.")
        else:
            print(f"Cinema bar sold {element.food} to {customer}.")
