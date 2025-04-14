from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    _hall = CinemaHall(hall_number)
    _cleaner = Cleaner(cleaner)
    list_of_customers = []

    for _customer in customers:
        list_of_customers.append(Customer(_customer["name"],
                                          _customer["food"]))

    for _customer in list_of_customers:
        CinemaBar.sell_product(_customer, _customer.food)

    _hall.movie_session(movie, list_of_customers, _cleaner)
