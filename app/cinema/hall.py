from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customer: list[Customer],
                      cleaning_staff: Cleaner) -> None:
        print(f'\"{movie_name}\" started in hall number {self.number}')
        for custome in customer:
            custome.watch_movie(movie=movie_name)
        print(f'\"{movie_name}\" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
