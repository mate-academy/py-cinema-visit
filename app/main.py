from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    list_customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cinema_hall_number = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    hall_clean = Cleaner(cleaning_staff)
    for customer in list_customers:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall_number.movie_session(movie_name, list_customers, hall_clean)
