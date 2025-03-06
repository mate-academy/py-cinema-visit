from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    result_list = []
    for element in customers:
        result_list.append(Customer(element["name"], element["food"]))
    for customer in result_list:
        CinemaBar.sell_product(customer.food, customer)
    for element in result_list:
        CinemaHall.movie_session(movie, element.name, cleaner)
