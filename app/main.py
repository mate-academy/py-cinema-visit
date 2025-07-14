from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customer_instances: List[Customer] = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    cleaner_instance: Cleaner = Cleaner(name=cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall: CinemaHall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_instances,
                       cleaning_staff=cleaner_instance)
