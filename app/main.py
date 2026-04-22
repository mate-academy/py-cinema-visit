from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: Cleaner,
    movie: str
) -> None:
    cleaner = Cleaner(cleaner)
    customers_obj = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer, customer.food)
        customers_obj.append(customer)
    CinemaHall(hall_number).movie_session(movie, customers_obj, cleaner)
