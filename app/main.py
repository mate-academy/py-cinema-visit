from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    actual_film = CinemaBar()
    customer_list = []
    for new_customer in customers:
        new_customer = Customer(new_customer["name"], new_customer["food"])
        customer_list.append(new_customer)
        actual_film.sell_product(new_customer.food, new_customer)
    current_cleaner = Cleaner(cleaner)
    current_session = CinemaHall(hall_number)
    current_session.movie_session(movie, customer_list, current_cleaner)
