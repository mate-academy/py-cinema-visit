from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    customer_instances = []
    for customer in customers:
        customer_obj = Customer(customer.get("name"), customer.get("food"))
        customer_instances.append(customer_obj)
        CinemaBar.sell_product(customer_obj.food, customer_obj)
    hall = CinemaHall(hall_number)
    cleaner_worker = Cleaner(cleaner)
    hall.movie_session(movie, customer_instances, cleaner_worker)
