from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_customers = []
    for customer in customers:
        created_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(created_customer.food, created_customer)
        list_customers.append(created_customer)
    CinemaHall(hall_number).movie_session(
        movie,
        list_customers,
        Cleaner(cleaner)
    )
