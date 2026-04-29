from app.cinema.customer import Customer

class CinemaBar:

    @staticmethod
    def sell_product(customer: "Customer", product: str):
        print(f"Cinemabar sold {product} to {customer.name}")
