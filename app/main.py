from typing import List


from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: List[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = [Customer(*customer.values()) for customer in customers]
    cleaning_stuff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_list, cleaning_stuff)
