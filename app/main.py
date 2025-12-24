from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    custom = [Customer(customers[i]["name"],
                customers[i]["food"]) for i in range(len(customers))]
    hl = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    for cust in custom:
        CinemaBar.sell_product(cust.food, cust)
    hl.movie_session(movie, custom, clean)
