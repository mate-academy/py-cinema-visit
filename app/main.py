from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List, Dict


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = [Customer(cm["name"], cm["food"]) for cm in customers]

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_instance
    )
