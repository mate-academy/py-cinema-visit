from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_instances = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_instances, cleaner)
