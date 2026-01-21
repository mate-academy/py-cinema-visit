from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_customers = [Customer(customer["name"], customer["food"])
                      for customer in customers]
    for customer in list_customers:
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall(hall_number).movie_session(
        movie,
        list_customers,
        Cleaner(cleaner)
    )
