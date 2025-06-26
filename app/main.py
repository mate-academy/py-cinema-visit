from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for elem in customers:
        customers_list.append(Customer(**elem))
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for elem in customers_list:
        CinemaBar.sell_product(elem, elem.food)
    hall.movie_session(movie, customers_list, cleaner)
