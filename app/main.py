from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    customer_instances = []
    for cust in customers:
        customer_instance = Customer(cust["name"], cust["food"])
        customer_instances.append(customer_instance)
        CinemaBar().sell_product(customer_instance, customer_instance.food)

    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
