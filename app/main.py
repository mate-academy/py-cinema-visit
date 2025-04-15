from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[str],
        hall_number: int,
        cleaner: str,
        movie: str
) -> str:
    customers = [Customer(**customer) for customer in customers]
    cleaner = Cleaner(cleaner)
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers, cleaner)
