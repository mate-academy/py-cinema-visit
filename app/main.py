from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cb = CinemaBar()
    list_customers = []

    for i, customer in enumerate(customers):
        list_customers.append(Customer(customer["name"], customer["food"]))
        cb.sell_product(list_customers[i], list_customers[i].food)

    ch = CinemaHall(hall_number)
    anna = Cleaner(cleaner)
    ch.movie_session(movie, list_customers, anna)
