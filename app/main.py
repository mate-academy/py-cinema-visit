from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_instances = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall_instance.movie_session(movie, customer_instances, cleaner_instance)
