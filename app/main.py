from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: Cleaner,
                 movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    customer_instances = [Customer(**customer) for customer in customers]

    for customer in customer_instances:
        cb.sell_product(customer=customer,
                        product=customer.food)

    ch.movie_session(movie_name=movie,
                     customers=customer_instances,
                     cleaning_staff=cleaner_instance)
