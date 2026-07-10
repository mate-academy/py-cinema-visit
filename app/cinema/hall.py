class CinemaHall:
    """
    Describes actions during the movie session
    """

    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaning_staff: Cleaner) ->:
        """
        This method prints about movie start, calls customers method
        watch_movie, prints about movie end, calls cleaner method clean_hall

        :param movie_name:
        :param customers:
        :param cleaning_staff:
        :return:
        """

        print(f"\"{movie_name}\" started in hall number {self.number}")

        for customer in customers:
            customer.watch_movie(movie_name)