from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects: list[Customer] = []

    for customer in customers:
        customer_object: Customer = Customer(
            customer["name"],
            customer["food"]
        )
        customer_objects.append(customer_object)
        CinemaBar.sell_product(customer_object.food, customer_object)

    cleaner_object: Cleaner = Cleaner(cleaner)
    cinema_hall_object: CinemaHall = CinemaHall(hall_number)

    cinema_hall_object.movie_session(
        movie,
        customer_objects,
        cleaner_object
    )
