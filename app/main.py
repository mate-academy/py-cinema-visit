from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    customer_list = [
        Customer(visitor["name"], visitor["food"]) for visitor in customers
    ]
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaning_staff)

    for customer in customer_list:
        cinema_bar.sell_product(customer, customer.food)
    hall.movie_session(movie_name, customer_list, clean)
