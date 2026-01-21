from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    cleaning_staff = Cleaner(cleaner)
    new = list()
    for cust in customers:
        customer = Customer(cust['name'], cust['food'])
        new.append(customer)
        bar.sell_product(customer.food, customer)
    n_hall = CinemaHall(hall_number)
    n_hall.movie_session(movie, new, cleaning_staff)
