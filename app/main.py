from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    cinema_bar = CinemaBar()
    for index, customer in enumerate(customers):
        customer_instance = Customer(customer["name"], customer["food"])
        customers_list.append(customer_instance)
        cinema_bar.sell_product(customer["food"], customers_list[index])

    hall_number_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    hall_number_instance.movie_session(movie, customers_list, cleaner_instance)
