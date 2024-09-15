from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cleaner = Cleaner(cleaner)
    client_list = [
        Customer(customer["name"], customer["food"]) for customer in customers]
    for customer in client_list:
        CinemaBar().sell_product(customer, customer.food)
    CinemaHall(hall_number).movie_session(movie, client_list, cleaner)
