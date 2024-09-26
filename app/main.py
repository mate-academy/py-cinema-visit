from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    for index, customer in enumerate(customers):
        customers[index] = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customers[index].food, customers[index])
    CinemaHall.movie_session(
        CinemaHall(hall_number), movie, customers, Cleaner(cleaner)
    )
