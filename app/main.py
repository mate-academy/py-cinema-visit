from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str,
                 ) -> None:
    visitors = list()
    for customer in customers:
        visitors.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    for visitor in visitors:
        CinemaBar.sell_product(visitor.food, visitor)
    hall.movie_session(movie, visitors, cleaner_staff)
