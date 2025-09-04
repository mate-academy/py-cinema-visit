from app.people.customer import Customer


class CinemaBar:  # Class that represents cinema bar.
    @staticmethod
    # Static method that sells food to customer.
    def sell_product(product: str, customer: Customer) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")

    def watch_movie(self, movie_name: str) -> None:
        print(f'{self.name} is watching "{movie_name}"')
