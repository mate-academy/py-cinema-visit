from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    chall = CinemaHall(hall_number)
    cbar = CinemaBar()
    ccleaner = Cleaner(cleaner)
    ccustomers = []
    for cust_item in customers:
        cust = Customer(cust_item["name"], cust_item["food"])
        cbar.sell_product(cust, cust.food)
        ccustomers.append(cust)
    chall.movie_session(movie, ccustomers, ccleaner)
