# app/people/customer.py


class Customer:
    def __init__(self, name: str, food: str) -> None:
        """Initialize with customer name and desired food."""
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """Simulate the customer watching a movie."""
        print(f'{self.name} is watching "{movie}".')
