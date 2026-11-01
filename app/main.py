from typing import List, Dict
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.bar import CinemaBar
from app.hall import CinemaHall


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = []

    for cust_data in customers:
        customer = Customer(name=cust_data["name"], food=cust_data["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
