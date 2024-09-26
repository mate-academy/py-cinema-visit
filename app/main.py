
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    customers_l = []
    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        customers_l.append(customer)
        cinema_bar.sell_product(customer_info["food"], customer)
    cinema_hall.movie_session(movie, customers_l, cleaner)
