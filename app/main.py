from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    total = [Customer(cust["name"], cust["food"]) for cust in customers]
    instance_cinema_hall = CinemaHall(hall_number)
    instance_cinema_bar = CinemaBar()
    instance_clear = Cleaner(cleaner)
    for cust in total:
        instance_cinema_bar.sell_product(cust.food, cust)
    instance_cinema_hall.movie_session(movie, total, instance_clear)
