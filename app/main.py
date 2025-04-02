from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from typing import List


def cinema_visit(
        customers: List[dict],
        hall_number: int,
        cleaner_name: str,
        movie_name: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner_name)

    customer_objects = [Customer(
        name=customer_data["name"],
        food=customer_data["food"]) for customer_data in customers]

    for customer in customer_objects:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
