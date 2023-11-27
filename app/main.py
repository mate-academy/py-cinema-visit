from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: list[{}],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    new_customers = []

    for customer in customers:
        new_customers.append(Customer(customer["name"], customer["food"]))
        CinemaBar.sell_product(
            customer["food"],
            Customer(customer["name"], customer["food"])
        )

    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    hall_number.movie_session(movie, new_customers, cleaner)
