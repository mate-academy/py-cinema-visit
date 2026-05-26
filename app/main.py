from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_instances = [Customer(customer["name"], customer["food"]) for
                          customer in customers]
    [CinemaBar.sell_product(customer.food, customer) for customer in
     customer_instances]
    CinemaHall(hall_number).movie_session(movie, customer_instances,
                                          Cleaner(cleaner))
