from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    bar = CinemaBar()

    bar_customers_list = [
        Customer(current_customer["name"], current_customer["food"])
        for current_customer in customers
    ]

    for current_customer in bar_customers_list:
        bar.sell_product(current_customer, current_customer.food)

    hall.movie_session(movie, bar_customers_list, current_cleaner)
