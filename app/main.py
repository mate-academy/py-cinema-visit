from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    customers_lst = []
    for customer in customers:
        name = customer["name"]
        custom = Customer(name, customer["food"])
        customers_lst.append(custom)
        cinema_bar.sell_product(custom, custom.food)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, customers_lst, cleaning_staff)
