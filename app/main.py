from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    cinema_guests = []
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)

    for i in customers:
        customer = Customer(i["name"], i["food"])
        cinema_guests.append(customer)
        CinemaBar.sell_product(customer, i["food"])
    CinemaHall.movie_session(hall_number, movie, cinema_guests, cleaner)
