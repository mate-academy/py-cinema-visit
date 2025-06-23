from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    guests = []
    for custom in customers:
        guest = Customer(custom["name"], custom["food"])
        guests.append(guest)
        CinemaBar.sell_product(guest.food, guest)
    cleaner = Cleaner(cleaner)
    session = CinemaHall(hall_number)
    session.movie_session(movie, guests, cleaner)
