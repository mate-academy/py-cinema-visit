from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[Customer],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    visited_customers = list()

    for customer in customers:
        visited_customer = Customer(name=customer.name, food=customer.food)
        CinemaBar.sell_product(name=customer.name, food=customer.food)
        visited_customers.append(visited_customer)

    hall.movie_session(
        movie_name=movie,
        customers=visited_customers,
        cleaning_staff=cleaning_staff,
    )
