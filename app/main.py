from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_ls = []
    cb = CinemaBar()
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_ls.append(customer)
        cb.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customers_ls, cleaner)
