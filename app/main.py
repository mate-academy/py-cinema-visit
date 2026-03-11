from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:

    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie,
        customers_list,
        Cleaner(cleaner)
    )
