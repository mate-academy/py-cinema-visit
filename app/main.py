# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:
    customers_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    cinema_bar = CinemaBar()
    for customer in customers_instances:
        cinema_bar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie_name, customers_instances, cleaner)
