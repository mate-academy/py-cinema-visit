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

    customer_instance = [
        Customer(customer["name"], customer.get("food"))
        for customer in customers
    ]

    janitor = Cleaner(cleaner)
    for customer in customer_instance:
        CinemaBar.sell_product(customer, customer.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie,
        customer_instance,
        janitor
    )
