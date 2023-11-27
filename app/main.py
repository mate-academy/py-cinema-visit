from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_instances = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers
    ]
    cinema_bar_instances = CinemaBar()
    cinema_hall_instances = CinemaHall(hall_number)
    cleaner_inst_instances = Cleaner(cleaner)
    for instance in customers_instances:
        cinema_bar_instances.sell_product(instance.food, instance)
    cinema_hall_instances.movie_session(
        movie,
        customers_instances,
        cleaner_inst_instances
    )
