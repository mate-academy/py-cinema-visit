from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    clients = [Customer(customer["name"], customer["food"])
               for customer in customers]
    stuff = Cleaner(cleaner)
    hall = CinemaHall(hall_number)

    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        bar.sell_product(customer.food, customer)
    return hall.movie_session(movie, clients, stuff)
