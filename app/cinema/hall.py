from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers_list: list,
            cleaning_staff: "Cleaner"
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')

        for person in customers_list:
            person.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
