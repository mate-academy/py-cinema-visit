from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    guests = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for guest in guests:
        bar.sell_product(guest.food, guest)
    hall.movie_session(movie, guests, cleaner)
