class Customer:
    """
    Customer class represents people coming into cinema
    to watch a movie. It contains functionality
    for watching a movie and stores information about name
    and food of a customer.
    """
    def __init__(self, name: str, food: str) -> None:
        self.name = name
        self.food = food

    def watch_movie(self, movie: str) -> None:
        """
        Function for informing that customer is watching given movie.
        :param movie: movie name to be watched by customer
        :return: None
        """
        print(f'{self.name} is watching "{movie}".')
