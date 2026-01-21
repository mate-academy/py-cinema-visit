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
    cinema_customers = [Customer(c["name"], c["food"]) for c in customers]
    cinema_bar = CinemaBar()
    for customer in cinema_customers:
        cinema_bar.sell_product(customer, customer.food)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, cinema_customers, Cleaner(cleaner))
    cleaner = Cleaner(cleaner)
