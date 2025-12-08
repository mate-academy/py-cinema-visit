from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) \
        -> None:
    cb = CinemaBar()
    session = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)
    customers_in_the_cinema = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    for customer in customers_in_the_cinema:
        cb.sell_product(customer, customer.food)

    session.movie_session(movie, customers_in_the_cinema, cinema_cleaner)
