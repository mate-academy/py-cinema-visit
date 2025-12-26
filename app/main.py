from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaning_staff: str,
    movie_name: str,
) -> None:
    customer_instances = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    cleaner = Cleaner(cleaning_staff)

    for customer_instance in customer_instances:
        cinema_bar.sell_product(
            customer=customer_instance, product=customer_instance.food
        )

    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customer_instances,
        cleaning_staff=cleaner
    )

    return customer_instances
