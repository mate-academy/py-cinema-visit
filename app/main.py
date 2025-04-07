from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    current_customers = [
        (Customer(customer["name"], customer["food"]))
        for customer in customers
    ]

    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)

    for customer in current_customers:
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, current_customers, staff)
