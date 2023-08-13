from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_cust_examples = [Customer(**visitor) for visitor in customers]
    for customer in list_cust_examples:
        CinemaBar.sell_product(customer, customer.food)
    our_hall = CinemaHall(hall_number)
    our_hall.movie_session(movie, list_cust_examples, Cleaner(cleaner))
