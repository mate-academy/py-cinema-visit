from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    # write you code here
    custom_list = []
    cinema_hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        custom_list.append(customer_instance)
        CinemaBar.sell_product(customer["food"], customer_instance)

    cinema_hall_instance.movie_session(movie, custom_list, cleaner_instance)
