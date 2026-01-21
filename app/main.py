from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    viewers = []
    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        CinemaBar.sell_product(customer.food, customer)
        viewers.append(customer)

    CinemaHall(hall_number).movie_session(movie, viewers, Cleaner(cleaner))
