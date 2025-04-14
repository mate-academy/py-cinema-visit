from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    customers_list = [Customer(person["name"], person["food"])
                      for person in customers]

    bar = CinemaBar()
    for buyer in customers_list:
        bar.sell_product(buyer, buyer.food)

    CinemaHall(hall_number).movie_session(
        movie, customers_list, Cleaner(cleaner)
    )
