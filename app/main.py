from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    list_of_customers = []

    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        list_of_customers.append(cust)
        CinemaBar.sell_product(cust.food, cust)

    cinema = CinemaHall(hall_number)
    clear = Cleaner(cleaner)

    cinema.movie_session(movie, list_of_customers, clear)
