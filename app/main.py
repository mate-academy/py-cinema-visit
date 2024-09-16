from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[Customer],
        hull_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinema_hall = CinemaHall(hull_number)
    cinema_bar = CinemaBar()
    hall_cleaner = Cleaner(cleaner)

    for customer in customers:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers, hall_cleaner)
