from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # registry of customer instances
    customer_instances = []
    for cust_dict in customers:
        # instantiate Customer
        customer_obj = Customer(
            name=cust_dict["name"],
            food=cust_dict["food"]
        )
        customer_instances.append(customer_obj)

        # use static method to provision from concessions counter
        CinemaBar.sell_product(
            customer=customer_obj,
            product=customer_obj.food
        )

    # setup the Hall and Staff Instances
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    # run the Session
    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
