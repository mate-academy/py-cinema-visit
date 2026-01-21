from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]
    cinema_bar = CinemaBar()
    for customer in customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)
    cinema.movie_session(movie_name=movie,
                         customers=customers,
                         cleaning_staff=cleaner)
