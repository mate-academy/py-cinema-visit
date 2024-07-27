from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    bar = CinemaBar()

    for customer in customers:
        bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie, customers, cleaner)
