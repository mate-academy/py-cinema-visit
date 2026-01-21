from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]

    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    for visitor in customers:
        CinemaBar.sell_product(visitor.food, visitor)
    cinema_hall.movie_session(movie, customers, cinema_cleaner)
