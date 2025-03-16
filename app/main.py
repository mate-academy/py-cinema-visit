from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    inst_cust = []
    for customer in customers:
        inst_cust.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    clean = Cleaner(cleaner)

    for customer in inst_cust:
        bar.sell_product(customer, customer.food)
    hall.movie_session(movie, inst_cust, clean)
