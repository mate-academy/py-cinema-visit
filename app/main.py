from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_objects = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)
    for customer in customers_objects:
        CinemaBar.sell_product(customer.food, customer)
    hall_instance.movie_session(movie, customers_objects, cleaner_instance)
