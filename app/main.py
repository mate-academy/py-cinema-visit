from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_objects = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_objects, cleaner_obj)
