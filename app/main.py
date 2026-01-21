from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    created_customers = create_customer(customers)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in created_customers:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, created_customers, cleaning_staff)


def create_customer(customers: list) -> list[Customer]:
    return [Customer(c["name"], c["food"]) for c in customers]
