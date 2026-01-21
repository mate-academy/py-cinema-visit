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
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_customers = []
    for customer in customers:
        cinema_customer = Customer(customer.get("name"), customer.get("food"))
        cinema_bar.sell_product(cinema_customer, cinema_customer.food)
        cinema_customers.append(cinema_customer)
    cinema_hall.movie_session(movie, cinema_customers, cinema_cleaner)
