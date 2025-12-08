from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customers, cleaner)
