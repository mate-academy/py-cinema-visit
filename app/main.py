from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    customers_instances = []
    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        customers_instances.append(customer_obj)
        cinema_bar.sell_product(customer_obj.food, customer_obj)
    cinema.movie_session(movie, customers_instances, cleaner_obj)
