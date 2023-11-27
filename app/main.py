from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_inst = []
    for customer in customers:
        customer_inst.append(Customer(customer["name"], customer["food"]))
    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    clean = Cleaner(cleaner)
    for customer in customer_inst:
        bar.sell_product(customer, customer.food)
    hall.movie_session(movie, customer_inst, clean)
