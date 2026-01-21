from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    br = CinemaBar()

    for customer in customers:
        br.sell_product(customer, customer.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers, Cleaner(cleaner))
