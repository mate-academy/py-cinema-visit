from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_ls = [Customer(person['name'], person['food'])
                    for person in customers]

    bar = CinemaBar()

    for person in customers_ls:
        bar.sell_product(person, person.food)

    CinemaHall(hall_number).movie_session(
        movie, customers_ls, Cleaner(cleaner))
