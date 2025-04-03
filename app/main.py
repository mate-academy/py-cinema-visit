from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str, movie: str
) -> None:
    people = [Customer(i["name"], i["food"]) for i in customers]
    for customer in people:
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall(hall_number).movie_session(movie, people, Cleaner(cleaner))
