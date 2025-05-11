from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = []
    for customer_data in customers:
        customer_instance = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        CinemaBar.sell_product(
            customer=customer_instance,
            product=customer_data["food"]
        )
        customer_instances.append(customer_instance)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner, assigned_hall=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
