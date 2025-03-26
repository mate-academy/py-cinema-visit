from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in customers:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customers, cleaner)
