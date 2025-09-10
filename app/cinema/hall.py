class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.number = hall_number   # <-- тепер 'number', як вимагають тести

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: str
    ) -> None:
        print(f"\"{movie_name}\" started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie=movie_name)
        print(f"\"{movie_name}\" ended.")
        cleaning_staff.clean_hall(hall_number=self.number)
