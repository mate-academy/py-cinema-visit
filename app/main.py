from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    visitors = [
        Customer(name=people["name"],
                 food=people["food"]) for people in customers
    ]

    staff = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)

    for guest in visitors:
        CinemaBar.sell_product(customer=guest, product=guest.food)

    hall.movie_session(movie, visitors, staff)
