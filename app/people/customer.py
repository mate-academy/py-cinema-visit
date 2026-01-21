class Customer:
    def __init__(self, name: str, food: str) -> None:
        """Store name and desired food."""
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """Customer watches a movie."""
        print(f'{self.name} is watching "{movie}".')
