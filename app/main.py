from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_list = [Customer(customer["name"], customer["food"])
                     for customer in customers]

    for customer in customer_list:
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customer_list, cleaner)
