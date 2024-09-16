from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    custom_list = [Customer(customer["name"], customer["food"])
                   for customer in customers]
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in custom_list:
        CinemaBar.sell_product(customer.food, customer)
    hall_number.movie_session(movie_name=movie,
                              customers=custom_list,
                              cleaning_staff=cleaner)
