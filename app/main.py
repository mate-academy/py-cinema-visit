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

    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    current_customers = [Customer(customer["name"], customer["food"]) for customer in customers]

    for customer in current_customers:
        bar.sell_product(customer.food, customer)

    hall.movie_session(movie, current_customers, cleaner)
