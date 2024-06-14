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

    customer_instances = [Customer(customer["name"], customer["food"])
                          for customer in customers]

    cleaner_instance = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall_instance = CinemaHall(hall_number)

    cinema_hall_instance.movie_session(
        movie,
        customer_instances,
        cleaner_instance
    )
