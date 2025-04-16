# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cleaner = Cleaner(cleaner)
    customers = [Customer(**customer) for customer in customers]
    hall = CinemaHall(hall_number)
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customers, cleaner)
