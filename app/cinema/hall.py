from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list | object,
                      cleaning_staff: Cleaner) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for person in customers:
            if isinstance(person, Customer):
                human = person
            elif (isinstance(person, dict) and "name" in person
                  and "food" in person):
                human = Customer(person["name"], person["food"])
            else:
                raise ValueError(f"Invalid customer data: {person}")
            human.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')

        return cleaning_staff.clean_hall(self.number)
