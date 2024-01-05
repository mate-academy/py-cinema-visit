# app/main.py
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)

    customer_instances = [Customer(name=customer["name"],
                                   food=customer["food"])
                          for customer in customers]

    for customer_instance in customer_instances:
        cinema_bar.sell_product(customer=customer_instance,
                                product=customer_instance.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=Cleaner(name=cleaner)
    )
