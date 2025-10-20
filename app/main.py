from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 number: int,
                 cleaner: str, movie: str) -> None:

    customer_list = []
    for customer in customers:
        new_customer_instance = Customer(customer["name"], customer["food"])
        customer_list.append(new_customer_instance)

        CinemaBar.sell_product(customer["food"], new_customer_instance)

    hall = CinemaHall(number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaner)
