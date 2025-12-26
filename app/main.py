from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_in = []
    for customer in customers:
        cs = Customer(name=customer["name"], food=customer["food"])
        customer_in.append(cs)
        CinemaBar.sell_product(cs, cs.food)

    hall_in = CinemaHall(hall_number)
    cleaner_in = Cleaner(cleaner)

    hall_in.movie_session(movie, customer_in, cleaner_in)
