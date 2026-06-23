from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects: list[Customer] = []

    for customer in customers:
        CinemaBar.sell_product(
            customer["food"],
            customer["name"]
        )

        customer_objects.append(
            Customer(
                customer["name"],
                customer["food"]
            )
        )

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(
        movie,
        customer_objects,
        cleaner_obj
    )
