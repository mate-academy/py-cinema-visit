from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    # write you code here
    owf = []

    for customer in customers:
        own = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(product=own.food, customer=own)
        owf.append(own)

    chistka = Cleaner(cleaner)
    zall = CinemaHall(hall_number)
    zall.movie_session(movie, owf, chistka)
