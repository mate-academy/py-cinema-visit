from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
        spectators: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    persons = []

    for human in spectators:
        name = human["name"]
        food = human["food"]
        person = Customer(name, food)
        persons.append(person)
        CinemaBar.sell_product(person.food, person)

    CinemaHall(hall_number).movie_session(movie, persons, Cleaner(cleaner))
