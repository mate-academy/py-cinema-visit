from typing import List, Dict
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: List[Dict[str, str]],
        hall_number: int, cleaner: str,
        movie: str) -> None:
    cinema_bar: CinemaBar = CinemaBar()
    cinema_hall: CinemaHall = CinemaHall(number=hall_number)
    cleaner_instance: Cleaner = Cleaner(name=cleaner)

    for customer_info in customers:
        customer_instance: \
            Customer = Customer(name=customer_info["name"],
                                food=customer_info["food"])
        cinema_bar.sell_product(
            customer=customer_instance,
            product=customer_instance.food
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[
            Customer(
                name=customer_info["name"],
                food=customer_info["food"]
            )
            for customer_info in customers],
        cleaning_staff=cleaner_instance
    )
