from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    customer_instances = []

    for customer_info in customers:
        customer_instance = Customer(
            name=customer_info["name"],
            food=customer_info["food"]
        )
        CinemaBar.sell_product(
            customer=customer_instance,
            product=customer_info["food"]
        )
        customer_instances.append(customer_instance)

    CinemaHall(hall_number).movie_session(
        movie_name,
        customer_instances,
        Cleaner(name=cleaner)
    )
