from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_obj = [Customer(customer["name"], customer["food"])
                     for customer in customers]
    current_bar = CinemaBar()
    for customer in customers_obj:
        current_bar.sell_product(customer, customer.food)

    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)

    current_hall.movie_session(movie, customers_obj, current_cleaner)
