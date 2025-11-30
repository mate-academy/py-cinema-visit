from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objects = \
        [Customer(name=customer["name"], food=customer["food"])
            for customer in customers]

    for customer in customer_objects:
        CinemaBar.sell_product(customer, customer.food)
    cleaning_staff = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie, customer_objects, cleaning_staff)
