from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,
) -> None:
    # Backward compatibility for positional call:
    # cinema_visit(customers, hall_number, cleaner, movie)
    if (
        isinstance(movie, list)
        and isinstance(customers, int)
        and isinstance(hall_number, str)
    ):
        movie, customers, hall_number, cleaner = (
            cleaner,
            movie,
            customers,
            hall_number,
        )

    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    for cust in customer_objects:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj,
    )
