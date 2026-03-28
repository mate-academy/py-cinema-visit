from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from typing import List, Dict


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = []

    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        customers_list.append(customer)

    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_instance
    )
