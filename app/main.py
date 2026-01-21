from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict], hall_number: int, cleaning_staff: str, movie: str
) -> None:
    customers_class_instances = [
        Customer(person["name"], person["food"]) for person in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaning_staff)

    for customer in customers_class_instances:
        cb = CinemaBar()
        cb.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_class_instances, cleaning_staff)
