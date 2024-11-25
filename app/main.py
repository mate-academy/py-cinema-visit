from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    cinema_visitors = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaning_staff = Cleaner(cleaner)

    for visitor in cinema_visitors:
        cinema_bar.sell_product(visitor, visitor.food)
    cinema_hall.movie_session(movie, cinema_visitors, cleaning_staff)
