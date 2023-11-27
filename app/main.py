from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    visitors = []
    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))

    current_bar = CinemaBar()
    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)

    for visitor in visitors:
        current_bar.sell_product(visitor.food, visitor)
    current_hall.movie_session(movie, visitors, current_cleaner)
