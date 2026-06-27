from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str,
) -> None:
    customers_instances = []
    for customer in customers:
        customers_instances.append(Customer(customer["name"],
                                            customer["food"]))
        CinemaBar.sell_product(customer["food"], customers_instances[-1])
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)
    hall_instance.movie_session(
        movie,
        customers_instances,
        cleaner_instance
    )
