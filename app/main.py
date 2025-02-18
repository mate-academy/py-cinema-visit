from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cus_list = [Customer(**customer) for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    for element in cus_list:
        CinemaBar.sell_product(element.food, element)
    cinema_hall.movie_session(movie, cus_list, hall_cleaner)
