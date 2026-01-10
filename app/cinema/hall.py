class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list["Customer"]
                      , cleaning_staff: "Cleaner") -> None:
        for customer in customers:
            customer.watch_movie(movie_name)
        cleaning_staff.clean_hall(self.hall_number)