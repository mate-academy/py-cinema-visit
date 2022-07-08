from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number, cleaner, movie):
    customers = [Customer(name=customer["name"],
                          food=customer["food"])
                 for customer in customers]
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)
    cb = CinemaBar()
    for customer in customers:
        cb.sell_product(customer=customer, product=customer.food)
    CinemaHall.movie_session(hall_number, movie, customers, cleaner)
