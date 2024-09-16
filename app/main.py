from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from typing import List


def cinema_visit(movie_name: str,
                 customers_data: List[dict],

                 cinema_bar: CinemaBar,
                 cinema_hall: CinemaHall,
                 cleaner: Cleaner) -> None:

    customers = [Customer(name=data["name"],
                          food=data["food"]) for data in customers_data]
    for customer in customers:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    # Movie session
    cinema_hall.movie_session(movie_name=movie_name,
                              customers=customers,
                              cleaning_staff=cleaner)
