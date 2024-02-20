from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers = [Customer(info["name"], info["food"]) for info in customers]
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    worker = Cleaner(cleaner)
    for customer in customers:
        cinema_bar.sell_product(customer, product=customer.food)
    hall.movie_session(movie, customers, worker)
