from app.cinema.bar import CinemaBar as cb # sell_product 
from app.cinema.hall import CinemaHall as ch # movie_session
from app.cinema_staff import Cleaner # clean_hall



def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        cb.sell_products(customer.food, customer.name)
    ch.movie_session(movie, customers, cleaner, hall_number)
