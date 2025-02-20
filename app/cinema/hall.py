from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self,
                      movie_name: str,
                      customers: list,
                      cleaning_staff: Cleaner) -> None:
        print(f""""{movie_name}" started in hall number {self.number}.""")

        for person in customers:
            person.watch_movie(movie_name)

        print(f""""{movie_name}" ended.""")

        print(f"Cleaner {cleaning_staff.name} "
              f"is cleaning hall number {self.number}.")
