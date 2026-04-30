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
    customer_instances = []
    for customer in customers:
        new_customer = Customer(**customer)
        CinemaBar.sell_product(new_customer, new_customer.food)
        customer_instances.append(new_customer)

    hall = CinemaHall(number=hall_number)
    staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_instances, staff)
