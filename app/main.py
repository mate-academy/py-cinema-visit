from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_customer = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in cinema_customer:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, cinema_customer, cleaner)
