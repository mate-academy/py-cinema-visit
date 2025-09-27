from people.customer import Customer


class CinemaBar:

    @staticmethod
    def sell_product(customer: "Customer", product: str) -> str:
        return f"Cinema bar sold {product} to {customer.name}"
