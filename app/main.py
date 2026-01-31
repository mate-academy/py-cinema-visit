from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:
    customer_instances = []
    for customer in customers:
        customer_instances.append(Customer(customer["name"], customer["food"]))

    for customer_instance in customer_instances:
        CinemaBar.sell_product(customer_instance.food, customer_instance)

    CinemaHall(hall_number).movie_session(movie,
                                          customer_instances, Cleaner(cleaner))
