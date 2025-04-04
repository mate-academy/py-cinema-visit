from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cleaner_ = Cleaner(cleaner)
    customers_ = [Customer(customer.get("name"),
                           customer.get("food")) for customer in customers]
    for customer in customers_:
        CinemaBar.sell_product(customer.food, customer.name)
    CinemaHall(hall_number).movie_session(movie, customers_, cleaner_)
