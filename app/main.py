from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    customer_list = []
    for customer in customers:
        name = customer["name"]
        name_cust = Customer(name, customer["food"])
        customer_list.append(name_cust)
        cinema_bar.sell_product(name_cust, name_cust.food)
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_list, cinema_cleaner)
