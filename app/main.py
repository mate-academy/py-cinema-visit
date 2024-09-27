from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie_name: str) -> None:
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar
    guests_list = []

    for customer in customers:
        guest = Customer(customer["name"], customer["food"])
        guests_list.append(guest)

    for guest in guests_list:
        cinema_bar.sell_product(guest, guest.food)

    hall.movie_session(movie_name, guests_list, cleaner)
