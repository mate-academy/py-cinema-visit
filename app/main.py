from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaning_staff: str,
        movie: str) -> None:
    customers_list = []
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)

    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_list, cleaner)
