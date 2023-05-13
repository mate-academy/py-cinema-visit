from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers = [Customer(cust["name"], cust["food"]) for cust in customers]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    stuff = Cleaner(cleaner)
    for cust in customers:
        cinema_bar.sell_product(cust.food, cust)
    hall.movie_session(movie, customers, stuff)
