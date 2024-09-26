from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) \
        -> None:
    cinema_hall_instance = CinemaHall(hall_number)
    customer_instances = []
    for person in customers:
        customer_instance = Customer(person["name"], person["food"])
        customer_instances.append(customer_instance)
        CinemaBar.sell_product(customer_instance, customer_instance.food)
    cleaner_instance = Cleaner(cleaner)
    cinema_hall_instance.movie_session(movie_name=movie,
                                       customers=customer_instances,
                                       cleaning_staff=cleaner_instance)
