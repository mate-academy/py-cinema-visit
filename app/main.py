from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    customer_instances = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        cinema_bar.sell_product(customer.food, customer)
        customer_instances.append(customer)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
