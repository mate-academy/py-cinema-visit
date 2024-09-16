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

    guests = []
    for customer in customers:
        guests.append(Customer(customer["name"], customer["food"]))
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    clean_staff = Cleaner(cleaner)

    for guest in guests:
        cinema_bar.sell_product(guest, guest.food)
    cinema_hall.movie_session(movie, guests, clean_staff)
