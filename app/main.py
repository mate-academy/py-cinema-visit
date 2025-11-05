from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer = [Customer(customers[i]["name"],
                customers[i]["food"]) for i in range(len(customers))]
    hl = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for cust in customer:
        CinemaBar.sell_product(cust.food, cust)
    CinemaHall.movie_session(hl, movie, customer, cleaner)
