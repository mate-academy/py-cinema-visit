from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str) -> None:
    new_person = [Customer(person["name"], person["food"])
                  for person in customers]
    for person in new_person:
        CinemaBar.sell_product(person.food, person)
    CinemaHall(hall_number).movie_session(movie, new_person, Cleaner(cleaner))
