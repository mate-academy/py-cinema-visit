from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaning_stuff = Cleaner(cleaner)

    for customer in customers:
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers, cleaning_stuff)
