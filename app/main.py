from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: Cleaner,
                 movie: str
                 ) -> None:
    customer_instances = [Customer(c["name"], c["food"]) for c in customers]
    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)

    cb = CinemaBar

    for customer in customer_instances:
        cb.sell_product(customer.food, customer)

    hall_instance.movie_session(movie, customer_instances, cleaner_instance)

