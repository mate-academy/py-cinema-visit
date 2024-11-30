from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers, Cleaner(cleaner))
