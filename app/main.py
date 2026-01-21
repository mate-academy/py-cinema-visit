from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers
    ]

    for cs in customers_list:
        CinemaBar.sell_product(cs, cs.food)

    CinemaHall(hall_number).movie_session(movie,
                                          customers_list,
                                          Cleaner(cleaner))
