from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    visitors = []
    number = CinemaHall(hall_number)
    staff = Cleaner(cleaning_staff)
    for visitor in customers:
        visitor = Customer(visitor["name"], visitor["food"])
        visitors.append(visitor)
        CinemaBar.sell_product(visitor.food, visitor)
    number.movie_session(movie_name, visitors, staff)
