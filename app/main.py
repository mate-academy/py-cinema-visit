from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    new_customers = []
    bar = CinemaBar()
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        new_customers.append(new_customer)
        bar.sell_product(new_customer.food, new_customer)
    hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    hall.movie_session(movie, new_customers, hall_cleaner)
