from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_instances = [Customer(name=customer["name"],
                                   food=customer["food"])
                          for customer in customers]

    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customer_instances, cleaner)
