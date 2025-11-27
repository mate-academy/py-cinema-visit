from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_list = []
    for customer in customers:
        man = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer["food"], man)
        customer_list.append(man)
    real_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customer_list, real_cleaner)
