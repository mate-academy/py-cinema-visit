class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff: "Cleaner") -> None:
        print(f"Movie '{movie_name}' in hall {self.hall_number} started.")


        for custom in customers:
            customer.wathc_movie(movie_name)

        print(f"Movie '{movie_name}' in hall {self.hall_number} finished.")

        cleaning_staff.clean_hall(self.hall_number)