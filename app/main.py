from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []

    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        customers_list.append(customer)

    bar = CinemaBar()
    for customer in customers_list:
        bar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customers_list, cleaner)
