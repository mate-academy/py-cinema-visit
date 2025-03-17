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

    customers_objects = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_objects:
        CinemaBar.sell_product(
            customer.food,
            customer
        )

    CinemaHall(hall_number).movie_session(
        movie,
        customers_objects,
        Cleaner(name=cleaner)
    )
