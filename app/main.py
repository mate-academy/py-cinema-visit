from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    visitors = [Customer(customer_dict["name"],
                         customer_dict["food"])
                for customer_dict in customers]

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for visitor in visitors:
        CinemaBar.sell_product(visitor.food, visitor)

    hall.movie_session(movie, visitors, cleaning_staff)
