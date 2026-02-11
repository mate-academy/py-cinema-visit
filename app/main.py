from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    custs = []
    for cust in customers:
        custs.append(Customer(cust["name"], cust["food"]))
    cleaner1 = Cleaner(cleaner)
    cinemahall1 = CinemaHall(hall_number)
    for cust in custs:
        CinemaBar.sell_product(cust.food, cust)
    cinemahall1.movie_session(movie, custs, cleaner1)
