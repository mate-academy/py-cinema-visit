from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers, hall_number, cleaner, movie):
    list_of_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers]
    cleaner = Cleaner(cleaner)
    hall_number = CinemaHall(hall_number)
    for customer in list_of_customers:
        CinemaBar.sell_product(customer, customer.food)
    CinemaHall.movie_session(hall_number, movie, list_of_customers, cleaner)
