from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customer_instances:
        CinemaBar().sell_product(product=customer.food, customer=customer)

    CinemaHall(number=hall_number).movie_session(
        movie_name=movie_name,
        customers=customer_instances,
        cleaning_staff=Cleaner(name=cleaner)
    )
