from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_obj = []
    for guest in customers:
        customer_obj.append(Customer(guest["name"], guest["food"]))
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    for guest in customer_obj:
        CinemaBar.sell_product(guest.food, guest)
    hall.movie_session(movie, customer_obj, cleaner_obj)
