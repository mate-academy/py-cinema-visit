# write your imports here
from typing import TypedDict
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


class CustomerStats(TypedDict):
    name: str
    food: str


def cinema_visit(
        movie: str,
        customers: list[CustomerStats],
        hall_number: int,
        cleaner: str
) -> None:
    cleaner_staff = Cleaner(cleaner)
    customers_list = [Customer(customer["name"], customer["food"])
                      for customer in customers]
    cinema_hall = CinemaHall(hall_number)

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_list, cleaner_staff)
