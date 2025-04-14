from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    list_of_customers = []
    for customer in customers:
        customer_instance = Customer(
            customer["name"],
            customer["food"]
        )
        CinemaBar.sell_product(
            customer_instance,
            customer["food"])
        list_of_customers.append(customer_instance)
    CinemaHall(hall_number).movie_session(
        movie,
        list_of_customers,
        Cleaner(cleaner))
