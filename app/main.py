from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    persons = []
    for person in customers:
        person["name"] = Customer(person["name"], person["food"])
        CinemaBar.sell_product(person["food"], person["name"])
        persons.append(person["name"])
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    CinemaHall.movie_session(hall, movie, persons, cleaner)
