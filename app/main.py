from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    temp_bar = CinemaBar()
    for customer in customers_list:
        temp_bar.sell_product(customer, customer.food)
    worker = Cleaner(cleaner)
    what_hall = CinemaHall(hall_number)
    what_hall.movie_session(movie, customers_list, worker)
