from typing import List
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar: CinemaBar = CinemaBar()
    cinema_hall: CinemaHall = CinemaHall(number=hall_number)
    cleaner: Cleaner = Cleaner(name=cleaner)

    customers_list: List[Customer] = [
        Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )for customer_data in customers
    ]

    for customer in customers_list:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
