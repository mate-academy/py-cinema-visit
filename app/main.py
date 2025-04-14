from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    customers_instances = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    for customer_instance in customers_instances:
        cinema_bar.sell_product(
            customer=customer_instance, product=customer_instance.food
        )

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instances,
        cleaning_staff=Cleaner(cleaner),
    )
