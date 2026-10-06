from typing import Any


from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict[str, Any]],
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    customers_list = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )

        customers_list.append(customer_instance)

        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )

    hall = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_instance
    )
