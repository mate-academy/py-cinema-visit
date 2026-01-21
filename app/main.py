from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    lst_of_guests = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    bar = CinemaBar()
    for guest in lst_of_guests:
        bar.sell_product(guest.food, guest)
    hall.movie_session(movie, lst_of_guests, staff)
