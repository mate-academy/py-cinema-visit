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
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    customer_instances = [
        Customer(**customer) for customer in customers
    ]
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_instances, cleaner)
