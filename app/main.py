from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    persons = []
    for customer in customers:
        persons.append(Customer(customer["name"], customer["food"]))
    for person in persons:
        CinemaBar.sell_product(person, person.food)
    CinemaHall(hall_number).movie_session(movie, persons, Cleaner(cleaner))
