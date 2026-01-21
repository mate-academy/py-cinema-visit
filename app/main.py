from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        number: int,
        cleaner: str,
        movie_name: str) -> None:

    people = []
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(person.food, person)
        people.append(person)

    CinemaHall(number).movie_session(movie_name, people, Cleaner(cleaner))
