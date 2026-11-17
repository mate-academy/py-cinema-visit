from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str) -> None:
    c_bar = CinemaBar()
    for customer in customers:
        c_obj = Customer(customer["name"], customer["food"])
        c_bar.sell_product(c_obj.food, c_obj)
    c_hall = CinemaHall(hall_number)
    c_staff = Cleaner(cleaner)
    c_hall.movie_session(movie, customers, c_staff)
