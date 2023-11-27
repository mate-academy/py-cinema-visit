from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    bar = CinemaBar()
    clean = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customers:
        bar.sell_product(customer.food, customer)

    hall.movie_session(movie, customers, clean)
