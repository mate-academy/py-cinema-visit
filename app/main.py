from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cinema_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    customers_l = []

    for new_customer in customers:
        new_customer = Customer(
            new_customer['name'],
            new_customer['food'],
        )
        customers_l.append(new_customer)

    for customer in customers_l:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customers_l, current_cleaner)
