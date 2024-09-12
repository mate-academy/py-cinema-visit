from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    cleaner, hall = Cleaner(cleaner), CinemaHall(hall_number)
    customer_lt = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer.food, customer)
        customer_lt.append(customer)
    hall.movie_session(movie, customer_lt, cleaner)
