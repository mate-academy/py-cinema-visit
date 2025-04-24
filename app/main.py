from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from typing import List


def cinema_visit(
        customers: List[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    list_customers = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        list_customers.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=list_customers,
        cleaning_staff=cleaning_staff
    )
