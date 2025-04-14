from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = []
    cinema_hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customers:
        customer_instances.append(Customer(customer["name"], customer["food"]))

    for bar_module in customer_instances:
        CinemaBar.sell_product(bar_module.food, bar_module)

    CinemaHall.movie_session(cinema_hall_instance, movie,
                             customer_instances, cleaner_instance)
