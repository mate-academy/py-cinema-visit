class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.number = hall_number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ):
        print(f"{movie_name} started in hall number {self.number}.")
        customer.watch_move(customers)
        print(f"{movie_name} ended.")
        cinema_staff.clean_hall(cleaning_staff)
