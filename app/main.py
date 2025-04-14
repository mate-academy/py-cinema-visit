from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    customers_list = [Customer(visitor["name"], visitor["food"])
                      for visitor in customers]

    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for visitor in customers_list:
        bar.sell_product(visitor, visitor.food)

    hall.movie_session(movie, customers_list, cleaner)
