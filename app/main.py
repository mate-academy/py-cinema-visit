from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(
            customer=customer_instance,
            product=customer["food"]
        )
        customer_instances.append(customer_instance)

    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=Cleaner(cleaner)
    )
