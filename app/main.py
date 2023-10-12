from typing import List


from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: List[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers, cleaner)
