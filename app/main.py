from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = []
    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        CinemaBar.sell_product(
            product=customer["food"],
            customer=customer_instance
        )
        customer_instances.append(customer_instance)

    CinemaHall(number=hall_number).movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=Cleaner(name=cleaner)
    )
