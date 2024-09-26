from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int, cleaner: str, movie: str
                 ) -> None:
    customers_instances = [
        Customer(**customer_data) for customer_data in customers
    ]
    cinema_bar = CinemaBar()
    for customer in customers_instances:
        cinema_bar.sell_product(customer, customer.food)
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_instances, cleaning_staff)
