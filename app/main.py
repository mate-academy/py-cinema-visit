from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str) -> None:
    customers_instances = []
    cinemahall = CinemaHall(hall_number)
    cinemabar = CinemaBar()
    cleaner = Cleaner(cleaning_staff)
    for human in customers:
        customer = Customer(human["name"], human["food"])
        customers_instances.append(customer)
        cinemabar.sell_product(customer.food, customer)
    cinemahall.movie_session(movie_name, customers_instances, cleaner)
