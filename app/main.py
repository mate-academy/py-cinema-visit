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

    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    current_customers = []

    for visitor in customers:
        current_customers.append(Customer(visitor["name"], visitor["food"]))

    for visitor in current_customers:
        CinemaBar.sell_product(visitor.food, visitor)
    current_hall.movie_session(movie, current_customers, current_cleaner)
