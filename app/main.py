from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    person = [Customer(client["name"], client["food"]) for client in customers]

    for customer in person:
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall(hall_number).movie_session(movie, person, Cleaner(cleaner))
