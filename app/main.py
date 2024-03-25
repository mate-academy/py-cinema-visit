# app/main.py
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner_name: str,
                 movie_name: str) -> None:

    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        cinema_bar.sell_product(customer, customer.food)

    hall.movie_session(movie_name,
                       [Customer(customer["name"],
                        customer["food"]) for customer in customers],
                       cleaner)
