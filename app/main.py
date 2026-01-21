from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    customer_instances = []
    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        customer_instances.append(customer)
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
