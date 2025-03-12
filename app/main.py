from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    customers_list = [Customer(customer["name"],
                               customer["food"]) for customer in customers]

    for customer in customers_list:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(cleaning_staff=cinema_cleaner,
                              customers=customers_list,
                              movie_name=movie)
