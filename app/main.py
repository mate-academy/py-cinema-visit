from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    people = []
    for customer in customers:
        people.append(Customer(customer["name"], customer["food"]))

    for person in people:
        cd = CinemaBar()
        cd.sell_product(person, person.food)

    ch = CinemaHall(hall_number)

    ch.movie_session(movie, people, Cleaner(cleaner))
