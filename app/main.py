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
    cinema_bar = CinemaBar()
    customers_list = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in customers_list:
        cinema_bar.sell_product(customer=customer, product=customer.food)
    CinemaHall(hall_number).movie_session(
        movie, customers_list, Cleaner(cleaner)
    )
