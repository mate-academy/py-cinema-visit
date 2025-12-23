from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_with_customers = []

    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(new_customer)
        list_with_customers.append(new_customer)

    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=list_with_customers,
        cleaning_staff=Cleaner(cleaner)
    )
