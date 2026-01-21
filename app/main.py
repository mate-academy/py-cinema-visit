from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) \
        -> None:
    customer_instances = []
    for customer_unit in customers:
        customer_instance = Customer(name=customer_unit["name"],
                                     food=customer_unit["food"])
        CinemaBar.sell_product(product=customer_unit["food"],
                               customer=customer_instance)
        customer_instances.append(customer_instance)

    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie, customers=customer_instances,
                       cleaning_staff=cleaning_staff)
