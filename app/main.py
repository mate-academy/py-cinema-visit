from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    customers_list = [Customer(customer["name"], customer["food"])
                      for customer in customers]

    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in customers_list:
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_list, cleaner)
