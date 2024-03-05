from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    for i, cstmr in enumerate(customers):
        customers[i] = Customer(cstmr["name"], cstmr["food"])
        CinemaBar.sell_product(customers[i].food, customers[i])
    CinemaHall(hall_number).movie_session(movie, customers, Cleaner(cleaner))
