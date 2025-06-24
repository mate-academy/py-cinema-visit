from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_visitors = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(new_customer.food, new_customer)
        cinema_visitors.append(new_customer)

    current_session = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    current_session.movie_session(movie, cinema_visitors, current_cleaner)
