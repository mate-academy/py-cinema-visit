from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    visitors = [Customer(person["name"], person["food"])
                for person in customers]
    number = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    for visitor in visitors:
        CinemaBar.sell_product(visitor.food, visitor)
    number.movie_session(movie, visitors, staff)
