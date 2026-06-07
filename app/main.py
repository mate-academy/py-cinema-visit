from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customers_cinema = []
    for customer in customers:
        customer_in_cinema = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer_in_cinema.food, customer_in_cinema)
        customers_cinema.append(customer_in_cinema)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie, customers_cinema, Cleaner(cleaner))
