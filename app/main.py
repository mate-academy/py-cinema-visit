from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    visitors = [Customer(cust["name"], cust["food"])
                for cust in customers]
    for cust in visitors:
        CinemaBar.sell_product(cust.food, cust)
    hall = CinemaHall(hall_number)
    cleaning = Cleaner(cleaner)
    hall.movie_session(movie, visitors, cleaning)
