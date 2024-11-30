class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_stuff: any
    ) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')

        for customer in customers:
            customer.watch_movie(movie=movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_stuff.clean_hall(hall_number=self.number)
