class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(
        self,
        movie_name: str,
        customers: list,
        cleaning_staff: str
    ) -> None:

        print(f"Movie '{movie_name}' is starting in hall {self.hall_number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie '{movie_name}' has ended")
        cleaning_staff.clean_hall(self.hall_number)
