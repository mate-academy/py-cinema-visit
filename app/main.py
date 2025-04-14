from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in visitors:
        cinema_bar = CinemaBar()
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, visitors, cleaner)
