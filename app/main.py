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
    cinema_visitors = []
    for item in customers:
        customer = Customer(item["name"], item["food"])
        CinemaBar.sell_product(customer, item["food"])
        cinema_visitors.append(customer)
    cinema = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema.movie_session(movie, cinema_visitors, cleaner)
