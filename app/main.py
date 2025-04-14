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
    list_of_cust = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        list_of_cust.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    ch = CinemaHall(hall_number)
    ch.movie_session(movie, list_of_cust, Cleaner(cleaner))
