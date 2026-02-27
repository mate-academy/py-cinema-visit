from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cust_list = []
    for customer in customers:
        clients = Customer(**customer)
        CinemaBar.sell_product(clients.food, clients)
        cust_list.append(clients)
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    hall.movie_session(movie, cust_list, clean)
