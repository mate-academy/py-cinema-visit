from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
    customers: List[Dict[str, str]],  # list of dicts with keys "name" and "food"
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customer_list = [
        Customer(
            c["name"],
            c["food"]
        )
        for c in customers
    ]

    for customer in customer_list:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    cinema_hall.movie_session(movie, customer_list, cleaning_staff)
