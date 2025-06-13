from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_instances = [
        Customer(d["name"], d["food"])
        for d in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    actual_cleaner = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_instances, actual_cleaner)
