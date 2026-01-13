from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    bar = CinemaBar()

    customers_obj = []

    for raw_customer in customers:
        new_customer = Customer(
            raw_customer['name'],
            raw_customer['food'],
        )
        customers_obj.append(new_customer)

    for customer in customers_obj:
        bar.sell_product(customer, customer.food)

    hall.movie_session(movie, customers_obj, current_cleaner)
