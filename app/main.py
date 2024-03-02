from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]
    for element in customers:
        CinemaBar.sell_product(customer=element, product=element.food)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers, Cleaner(cleaner))
