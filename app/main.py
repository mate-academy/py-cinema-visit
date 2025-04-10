from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for customer in customers:
        customers_list.append(Customer(customer['name'],
                                       customer['food']))
    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaner)
    for customer in customers_list:
        bar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_list, cleaner)
