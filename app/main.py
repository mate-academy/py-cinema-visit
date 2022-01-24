from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    current_hall.movie_session(movie, customers_list, current_cleaner)
