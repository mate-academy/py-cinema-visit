from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_obj = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_obj.append(customer_obj)

        CinemaBar.sell_product(customer["food"], customer_obj)

    hall = CinemaHall(hall_number)

    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie, customers_obj, cleaner_obj)
