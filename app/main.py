from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    created_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in created_customers:
        CinemaBar.sell_product(customer, customer.food)
    cinema_cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, created_customers, cinema_cleaner)
