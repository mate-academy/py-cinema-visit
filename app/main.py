from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    result = [Customer(people["name"], people["food"])
              for people in customers]
    for guest in result:
        CinemaBar.sell_product(guest.food, guest)
    CinemaHall(hall_number).movie_session(movie, result, Cleaner(cleaner))
