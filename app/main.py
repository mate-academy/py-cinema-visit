from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_instances = [Customer(customer["name"], customer["food"])
                          for customer in customers]
    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)
    cleaner_now = Cleaner(cleaner)
    cinema_now = CinemaHall(hall_number)
    cinema_now.movie_session(movie, customer_instances, cleaner_now)
