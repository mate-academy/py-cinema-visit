from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)
    customers_instances = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_instances.append(customer)
        CinemaBar.sell_product(customer, customer.food)

    CinemaHall.movie_session(
        movie_name=movie,
        cleaning_staff=cleaner,
        customers=customers_instances,
        self=hall_number
    )
