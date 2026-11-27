from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
# write your imports here


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_cinema_list = []
    for customer in customers:
        customer_cinema = Customer(customer["name"], customer["food"])
        customer_cinema_list.append(customer_cinema)
    ch = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer_cinema in customer_cinema_list:
        CinemaBar.sell_product(customer_cinema, customer_cinema.food)
    ch.movie_session(movie, customer_cinema_list, cleaner)