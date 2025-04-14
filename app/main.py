from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:
    customers_instances = []
    for customer_dict in customers:
        customer = Customer(customer_dict["name"], customer_dict["food"])
        customers_instances.append(customer)
        CinemaBar.sell_product(customer, customer.food)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    hall.movie_session(movie_name, customers_instances, cleaner)
