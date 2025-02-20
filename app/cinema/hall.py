class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: any) -> None:
        print(f'\"{movie_name}\" '
              f"started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'\"{movie_name}\" ended.')
        cleaning_staff.clean_hall(self.number)
