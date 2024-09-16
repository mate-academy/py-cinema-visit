from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_instances, cleaner)
