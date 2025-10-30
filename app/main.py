from typing import Iterable
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: Iterable[dict],
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:

    # Sell products & create customer objects
    customer_objects = []
    for data in customers:
        customer = Customer(name=data["name"], food=data["food"])
        CinemaBar.sell_product(customer=customer, product=customer.food)
        customer_objects.append(customer)

    # Start movie session
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaning_staff)
