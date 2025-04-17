from app.cinema.bar import CinemaBar
from app.cinema.bar import Customer
from app.cinema.hall import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers = [Customer(name=data["name"],
                          food=data["food"]) for data in customers]

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)

    cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customers,
                       cleaning_staff=cleaner)
