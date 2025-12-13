from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(customers: [dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_objects = [Customer(customer["name"],
                                  customer["food"])
                         for customer in customers]

    hall_object = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)

    for customer in customers_objects:
        CinemaBar.sell_product(customer, customer.food)

    hall_object.movie_session(movie, customers_objects, cleaner_object)
