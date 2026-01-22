from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> str:
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)
    cleaner = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customer_instances, cleaner)
