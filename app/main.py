from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall = CinemaHall(number=hall_number)

    cinema_hall.movie_session(
        movie, customer_objects, Cleaner(name=cleaner)
    )
